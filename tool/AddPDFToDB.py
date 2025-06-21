from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader

'''
    NOTE: Use your embedding model for embedding_function=
    at the place of MYEmbedding()
'''


# Tool Input Schema
class AddPDFToDBInput(BaseModel):
    pdf_path: str = Field(..., description="Local path to the PDF file")

# Tool Output Schema
class AddPDFToDBOutput(BaseModel):
    success: bool = Field(..., description="Whether the PDF was successfully added")

# Tool Class
class AddPDFToDB(BaseTool):
    name: str = "Add PDF to vector DB"
    description: str = "Adds a local PDF to the Chroma vector database"
    args_schema: Type[BaseModel] = AddPDFToDBInput
    return_schema: Type[BaseModel] = AddPDFToDBOutput

    def _run(self, pdf_path: str) -> AddPDFToDBOutput:
        try:
            loader = PyPDFLoader(pdf_path)
            documents = loader.load_and_split()

            # Use existing DB and append
            db = Chroma(persist_directory="chroma_db", embedding_function=MYEmbedding())
            db.add_documents(documents)

            return AddPDFToDBOutput(success=True)
        except Exception as e:
            print(f"Error: {e}")
            return AddPDFToDBOutput(success=False)

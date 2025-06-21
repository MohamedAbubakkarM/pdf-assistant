from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain_community.vectorstores import Chroma

'''
    NOTE: Use your embedding model for embedding_function=
    at the place of MYEmbedding()
'''


# Tool Input Schema
class RAGtoolInput(BaseModel):
    query: str = Field(..., description="Query to search the PDF")

# Tool Output Schema
class RAGtoolOutput(BaseModel):
    response: str = Field(..., description="Answer from the vector database")

# RAG Tool
class RAGtool(BaseTool):
    name: str = "Searches the PDF in the vector database"
    description: str = "Searches the vector DB for an answer to the query"
    args_schema: Type[BaseModel] = RAGtoolInput
    return_schema: Type[BaseModel] = RAGtoolOutput

    def _run(self, query: str) -> RAGtoolOutput:
        try:
            db = Chroma(persist_directory="chroma_db", embedding_function=MYEmbedding())

            results = db.similarity_search(query, k=5)

            if not results:
                return RAGtoolOutput(response="No relevant content found in the vector database.")

            for i, doc in enumerate(results):
                print(f"[Match {i+1}] {doc.page_content[:200]}...\n")  # Debugging

            answer = "\n\n".join([doc.page_content for doc in results])
            return RAGtoolOutput(response=answer)

        except Exception as e:
            return RAGtoolOutput(response=f"Error: {str(e)}")

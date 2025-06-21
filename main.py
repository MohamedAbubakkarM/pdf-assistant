from crewai import Crew, Agent, Task, LLM, Process
from tool.RAGtool import RAGtool
from tool.AddPDFToDB import AddPDFToDB

'''
        NOTE: Use LLM of your choice at the place of llm for Agent(), Crew()
'''

# Required tools
rag_tool = RAGtool()
vector_db_tool = AddPDFToDB()


# Agent definitions
embed_agent = Agent(
        role="Embed Agent",
        goal="Load the provided local PDF file and store it into the vector database for later semantic querying.",
        backstory="""
            Embed Agent is responsible for preparing documents for intelligent analysis.
            It specializes in accepting local PDF files provided by the user, validating their existence,
            and efficiently loading them into the vector database.

            Once a file is ingested, other agents can perform summarization, question-answering, and insight extraction tasks. 
            The Scrape Agent plays a crucial role in ensuring that only valid, readable documents are stored for downstream processing,
            and it acts as the first step in the research assistant's workflow.
        """,
        allow_delegation=False,
        verbose=True,
        tools=[vector_db_tool],
        llm=llm,
    )

summarize_agent = Agent(
        role="Summarizer Agent",
        goal="Summarize the intended section based on the user query",
        backstory=
        """ 
            Summarizer Agent has an excellent skill of scanning a section in the PDF
            and providing the user with an accurate and clearly understandable summary
            of that particular section.

            Your task is to locate the **exact section** based on the user query and provide
            a **structured and detailed summary** that includes all key points and insights.

            - Focus strictly on the section requested by the user.
            - Do not give generic or one-line responses.
            - The summary must reflect the original content accurately and clearly.
            - If the section is complex, break down the explanation into bullet points or simple sentences.
            - Avoid unrelated parts and do not add your own opinions.

            Always deliver a well-organized and clear summary.
        """,
        allow_delegation=False,
        verbose=True,
        tools=[vector_db_tool, rag_tool],
        llm=llm,
    )


# Tasks for agents
scraping_task = Task(
        description=(
            """
                Load the local PDF file provided by the user and store it into the vector database.
                The Scrape Agent will validate the file path, read the content, and make it available
                for downstream querying by other agents.

                Here's the path to the local PDF file:
                {pdf_path}
            """
        ),
        expected_output="""
            Find the correct PDF and store it in the vector database.
        """,
        tools=[vector_db_tool, rag_tool],
        agent=embed_agent,
)

summarizing_task = Task(
        description=(
            """
                Search through the PDF and extract detailed insights 
                specifically from the section titled or related to: {question}. 
                The answer must be a clear, concise, and accurate summary based strictly on the
                content in that section — not a generic or one-line response. If the section is long, provide a structured
                summary highlighting the key points, examples, and conclusions. Ignore unrelated parts of the document.
            """
        ),
        expected_output="""
            Provide a big summary of the section from the PDF.
            ***OUTPUT:***
            SUMMARY SHOULD BE IN POINTS.
        """,
        tools=[rag_tool],
        agent=summarize_agent,
    )

# Crew
crew = Crew(
        agents=[embed_agent, summarize_agent],
        tasks=[scraping_task, summarizing_task],
        process=Process.sequential,
        verbose=True,
)


question = input(
        "Enter the section you want to summarize\n"
    )

result = crew.kickoff({"pdf_path": r"path_to_your_local_pdf_file, "question": question})
print(result)








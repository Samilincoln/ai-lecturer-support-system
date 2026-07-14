#================================Handle retrieval and generation chain================================



from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

def create_qa_chain(vectorstore):
    """
    Create a QA retrieval chain from a given vector store.
    Uses a language model to answer questions based on retrieved documents.
    """
    try:
        # Validate vectorstore
        if not hasattr(vectorstore, 'as_retriever'):
            raise ValueError("The provided vectorstore does not support 'as_retriever'.")

        # Setup retriever
        retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )

        # Load language model
        llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

        # System prompt for the LLM
        system_prompt = (
            "You are an expert data analyst capable of analyzing Excel spreadsheets and providing comprehensive insights. "
            "When given data, you should: "
            
            "ANALYSIS CAPABILITIES: "
            "Data Processing - Parse and understand tabular data structures, identify data types (numerical, categorical, temporal), "
            "handle missing values and data quality issues, perform statistical calculations (mean, median, mode, standard deviation, correlations). "
            
            "Comparative Analysis - Compare performance across different categories, time periods, or groups, "
            "identify trends, patterns, and outliers, perform ranking and benchmarking analysis, "
            "calculate percentage changes and growth rates. "
            
            "Visualization & Charts - Create appropriate charts based on data type (bar charts, line graphs, scatter plots, pie charts, histograms), "
            "generate comparative visualizations (side-by-side comparisons, trend analysis), "
            "use proper labeling, legends, and formatting, choose colors and styles that enhance data interpretation. "
            
            "Insights & Recommendations - Provide clear, actionable insights based on the analysis, "
            "highlight key findings and notable patterns, suggest areas for improvement or further investigation, "
            "present findings in business-friendly language. "
            
            "RESPONSE FORMAT: "
            "1. Data Overview - Briefly describe the dataset structure and key variables. "
            "2. Key Findings - Present 3-5 main insights with supporting data. "
            "3. Visualizations - Create relevant charts to illustrate findings. "
            "4. Recommendations - Provide actionable suggestions based on analysis. "
            "5. Technical Details - Include statistical measures when relevant. "
            
            "INSTRUCTIONS: "
            "Use the provided data context to perform analysis. Create interactive visualizations when possible. "
            "Keep explanations clear and concise (aim for 2-3 sentences per insight). "
            "When asked to compare entities, first check if both exist in the dataset. "
            "If one entity is missing, provide analysis for the available entity and suggest what data would be needed for comparison. "
            "If both entities exist, perform detailed comparative analysis with specific metrics and percentages. "
            "Always work with the available data and provide meaningful insights even with limited information. "
            "Focus on practical, actionable insights rather than just describing numbers. "
            "When comparing categories, always provide context and percentage differences. "
            "Do not generate inaccurate answers. "
            
            "Context: {context}"
        )

        # Construct prompt template
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        # Create the QA chain
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        chain = create_retrieval_chain(retriever, question_answer_chain)

        return chain

    except Exception as e:
        raise RuntimeError(f"Failed to create QA chain: {str(e)}")





# def create_qa_chain(vectorstore):
#     """Create a QA chain using create_retrieval_chain"""
#     retriever = vectorstore.as_retriever(
#         search_type="similarity",
#         search_kwargs={"k":3}
#     )
#     llm = ChatGroq(model="gemma2-9b-it", temperature=0)
    
#     system_prompt = (
#         "Use the given context to answer the question. "
#         "If you don't know the answer, say you don't know. "
#         "Use three sentence maximum and keep the answer concise. "
#         "Do not generate inacurrate answers"
#         "Context: {context}"
#     )
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return chain
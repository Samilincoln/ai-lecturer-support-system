#=======================Convert df into document==================

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter



def df_to_document(df):
    """
    Convert a pandas DataFrame to a list of chunked Document objects
    suitable for retrieval or embedding.
    """
    try:
        if df.empty:
            raise ValueError("DataFrame is empty. Please provide a valid DataFrame.")

        # Convert each row of the DataFrame into a Document
        documents = [
            Document(page_content="\n".join(f"{col}: {row[col]}" for col in df.columns))
            for _, row in df.iterrows()
        ]

        # Split the documents into chunks for better processing
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", ".", ",", " ", ""]
        )

        chunked_documents = text_splitter.split_documents(documents)
        return chunked_documents

    except Exception as e:
        raise RuntimeError(f"Failed to convert DataFrame to documents: {str(e)}")





# def df_to_document(df):
#     # First create documents from dataframe rows
#     documents = [Document(page_content="\n".join(f"{col}: {row[col]}" for col in df.columns)) for _, row in df.iterrows()]
    
#     # Then chunk them into smaller pieces for better retrieval
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50,
#         separators=["\n\n", "\n", ".", ",", " ", ""]
#     )
    
#     chunked_documents = text_splitter.split_documents(documents)
#     return chunked_documents
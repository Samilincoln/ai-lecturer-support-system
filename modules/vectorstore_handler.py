#=============================Handle the vector store creation and loading================

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_cohere import CohereEmbeddings

load_dotenv()

embedding_api_key = os.getenv("EMBEDDING_API_KEY")  

VECTORSTORE_DIR = "vectorstore"
FAISS_INDEX = os.path.join(VECTORSTORE_DIR, "index.faiss")
METADATA_FILE = os.path.join(VECTORSTORE_DIR, "index.pkl")


# def save_vectorstore(vs):
#     """Save the vectorstore to local directory."""
#     try:
#         os.makedirs(VECTORSTORE_DIR, exist_ok=True)
#         vs.save_local(VECTORSTORE_DIR)
#     except Exception as e:
#         raise RuntimeError(f"❌ Error saving vectorstore: {str(e)}")


# def load_vectorstore():
#     """Load existing vectorstore from local directory."""
#     try:
#         if not embedding_api_key:
#             raise ValueError("OpenAI embedding API key not found in environment variables.")

#         if os.path.exists(FAISS_INDEX) and os.path.exists(METADATA_FILE):
#             embeddings = OpenAIEmbeddings(openai_api_key=embedding_api_key)  # ✅
#             return FAISS.load_local(
#                 VECTORSTORE_DIR,
#                 embeddings,
#                 allow_dangerous_deserialization=True
#             )
#         else:
#             return None
#     except Exception as e:
#         raise RuntimeError(f"❌ Error loading vectorstore: {str(e)}")


# def create_vectorstore(documents):
#     """Create new vectorstore from documents."""
#     try:
#         if not embedding_api_key:
#             raise ValueError("OpenAI embedding API key not found in environment variables.")

#         embeddings = OpenAIEmbeddings(openai_api_key=embedding_api_key)  # ✅
#         vs = FAISS.from_documents(documents, embeddings)
#         save_vectorstore(vs)
#         return vs
#     except Exception as e:
#         raise RuntimeError(f"❌ Error creating vectorstore: {str(e)}")

















embedding_api_key = os.getenv("EMBEDDING_API_KEY")

VECTORSTORE_DIR = "vectorstore"
FAISS_INDEX = os.path.join(VECTORSTORE_DIR, "index.faiss")
METADATA_FILE = os.path.join(VECTORSTORE_DIR, "index.pkl")

def save_vectorstore(vs):
    """Save the vectorstore to local directory"""
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)
    vs.save_local(VECTORSTORE_DIR)

def load_vectorstore():
    """Load existing vectorstore from local directory"""
    if os.path.exists(FAISS_INDEX) and os.path.exists(METADATA_FILE):
        embeddings = CohereEmbeddings(
            model="embed-v4.0",
            cohere_api_key=embedding_api_key,  
            user_agent="langchain"
        )
        return FAISS.load_local(VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
    return None

def create_vectorstore(documents):
    """Create new vectorstore from documents"""
    try:
        embeddings = CohereEmbeddings(
            model="embed-v4.0",
            cohere_api_key=embedding_api_key,
            user_agent="langchain"
        )
        vs = FAISS.from_documents(documents, embeddings)
        save_vectorstore(vs)
        return vs
    except Exception as e:
        print("❌ Error creating vectorstore:", e)
        raise e


































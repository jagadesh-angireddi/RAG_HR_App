from hr_assistant import config
import os

from hr_assistant.embeddings import get_embeddings_model

from langchain_community.vectorstores import FAISS


def build_vector_store(chunks):
    """Builds a Searchable vector store from the chunks"""

    embedding_model = get_embeddings_model()
    return FAISS.from_documents(chunks,embedding_model)

def save_vector_store(vector_store, path:str=config.VECTORE_STORE_PATH)->None:
    """Save the FAISS index to disk"""
    vector_store.save_local(path)

def load_vector_store(path:str=config.VECTORE_STORE_PATH):
    """Load a previous saved FAISS from disk"""

    embeddings_model=get_embeddings_model()
    return FAISS.load_local(path,embeddings_model, allow_dangerous_deserialization=True)

def vector_store_exists(path:str=config.VECTORE_STORE_PATH)->bool:
    """Checks if vectorstore is presnt or not"""
    return os.path.exists(os.path.join("path","index.faiss"))

def get_retriever(vector_store,k=config.TOP_K_RESULTS):
    """returns as retriever"""
    return vector_store.as_retriever(search_kwargs={"k":k})
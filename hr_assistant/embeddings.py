from langchain_community.embeddings import JinaEmbeddings

from hr_assistant import config

def get_embeddings_model():
    """Returns JinaEmbeddings model name and reads apikey"""
    return JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
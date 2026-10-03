import os
from dotenv import load_dotenv

load_dotenv()

#API VARIABLES

GROQ_API_KEY=os.getenv('GROQ_API_KEY')
JINA_API_KEY=os.getenv('JINA_API_KEY')




#DATA PATHS

DATA_PATH = os.path.join("data","hr_policy.txt")

VECTORE_STORE_PATH = os.path.join("data","faiss_index")

#LLM MODELS

LLM_MODEL_NAME="openai/gpt-oss-20b"

EMBEDDING_MODEL_NAME="jina-embeddings-v2-base-en"

#CHUNKS

CHUNK_SIZE=500
CHUNK_OVERLAP=50

#RETRIEVAL_RESULTS

TOP_K_RESULTS=3

#SYSTEM_INSTRCUTIONS

SYSTEM_PROMPT =( 

    "You are a friendly HR assistant working for Acme Crop."
    "Always use the search_hr_policy tool to look up"
    "facts before answering."
    "If the answer isn't in the search results, say you don't know "
    "instead of guessing." 


)

def check_api_keys() -> None:
    """Stop early with a clear message if a required API key is missing."""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it to your .env file.")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY. Please add it to your .env file.")
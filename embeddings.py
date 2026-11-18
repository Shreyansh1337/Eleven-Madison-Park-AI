
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_DIMENSIONS, EMBEDDING_MODEL, GEMINI_API_KEY


def get_embeddings():
    

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GEMINI_API_KEY,
        output_dimensionality=EMBEDDING_DIMENSIONS
    )

    return embeddings

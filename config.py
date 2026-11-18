
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )


DATA_FILE_PATH = BASE_DIR / "eleven_madison_park_data.txt"

CHUNK_SIZE = 750
CHUNK_OVERLAP = 150

EMBEDDING_MODEL = "gemini-embedding-001"
EMBEDDING_DIMENSIONS = 768


LLM_MODEL = "gemini-3.1-flash-lite"
LLM_TEMPERATURE = 0

RETRIEVAL_K = 3

CHROMA_DB_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "eleven_madison_park"

from langchain_chroma import Chroma

from config import CHROMA_DB_DIR, COLLECTION_NAME
from embeddings import get_embeddings
from ingestion import load_documents, split_documents


def create_vector_store():

    embeddings = get_embeddings()
   
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DB_DIR)
    )

    existing_count = vector_store._collection.count()

    if existing_count > 0:
        print(f"Loaded existing vector database ({existing_count} embeddings).")
        return vector_store

   
    print("No existing embeddings found. Creating them for the first time...")

    raw_documents = load_documents()
    chunks = split_documents(raw_documents)

    print(f"Loaded {len(raw_documents)} documents.")
    print(f"Created {len(chunks)} chunks.")
    print("Generating embeddings and saving to Chroma...")

    vector_store.add_documents(chunks)

    print(
        f"Successfully stored "
        f"{vector_store._collection.count()} embeddings."
    )

    return vector_store

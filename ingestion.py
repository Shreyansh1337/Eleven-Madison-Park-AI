
import re

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_OVERLAP, CHUNK_SIZE, DATA_FILE_PATH


def load_documents():
    

    text = DATA_FILE_PATH.read_text(encoding="utf-8")

    pattern = re.compile(
        r"^Source:\s*(?P<source>[^\r\n]+)\r?\n"
        r"Title:\s*(?P<title>[^\r\n]+)\r?\n"
        r"Content:\s*\r?\n?"
        r"(?P<content>.*?)\r?\n"
        r"---END OF SOURCE---",
        re.MULTILINE | re.DOTALL
    )

    matches = list(pattern.finditer(text))

    if not matches:
        raise ValueError("No webpage records found in the data file.")

    documents = []

    for match in matches:
        source = match.group("source").strip()
        title = match.group("title").strip()
        content = match.group("content").strip()

        if not content:
            continue

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": source,
                    "title": title
                }
            )
        )

    if not documents:
        raise ValueError("No documents with content were found.")

    return documents


def split_documents(raw_documents):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents(raw_documents)

    if not chunks:
        raise ValueError("Document splitting produced no chunks.")

    return chunks


if __name__ == "__main__":
    raw_documents = load_documents()
    chunks = split_documents(raw_documents)

    print(f"Loaded {len(raw_documents)} webpage documents.")
    print(f"Created {len(chunks)} chunks.")

    print("\nFirst document metadata:")
    print(raw_documents[0].metadata)

    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk preview:")
    print(chunks[0].page_content[:300])

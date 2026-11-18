# 🍽️ Eleven Madison Park — AI-Powered RAG Q&A Assistant
---

## 📌 Overview

**Eleven Madison Park AI Assistant** is a Retrieval-Augmented Generation (RAG) application that allows users to ask natural-language questions about Eleven Madison Park using information collected from the restaurant's official website.

Instead of relying entirely on an LLM's pretrained knowledge, the application retrieves relevant information from a custom vector database and provides it as context to Google Gemini to generate grounded answers.

The application also displays the source URLs used to generate each response, making the answers easier to verify.

## ✨ Features

- **Retrieval-Augmented Generation:** Combines semantic document retrieval with LLM-powered answer generation.
- **Website Data Ingestion:** Loads and processes restaurant website content.
- **Text Chunking:** Splits documents into smaller, overlapping chunks for effective retrieval.
- **Semantic Search:** Uses Gemini embeddings to identify contextually relevant information.
- **Persistent Vector Storage:** Stores embeddings in ChromaDB to avoid regenerating them every time the application starts.
- **Source Attribution:** Displays the source URLs associated with retrieved documents.
- **Interactive Interface:** Provides a simple question-answering interface built with Gradio.
- **Context-Grounded Responses:** Uses prompt engineering to instruct the LLM to answer using retrieved context rather than inventing information.

## 🛠️ Tech Stack

| Technology           | Purpose                         |
| -------------------- | ------------------------------- |
| Python               | Core programming language       |
| LangChain            | RAG pipeline and orchestration  |
| Google Gemini        | LLM for answer generation       |
| Gemini Embedding API | Text embeddings                 |
| ChromaDB             | Persistent vector database      |
| Gradio               | Interactive web interface       |
| Python-dotenv        | Environment variable management |

## 🏗️ Architecture

The application follows a basic Retrieval-Augmented Generation pipeline.

```text
       Restaurant Website Data
                 |
                 ▼
          Document Loading
                 |
                 ▼
            Text Splitting
                 |
                 ▼
         Gemini Embeddings
                 |
                 ▼
          ChromaDB Storage
                 |
                 |
       USER ENTERS A QUESTION
                 |
                 ▼
        Question Embedding
                 |
                 ▼
       Semantic Similarity Search
                 |
                 ▼
       Retrieve Top 3 Documents
                 |
                 ▼
       Context + User Question
                 |
                 ▼
          Google Gemini LLM
                 |
                 ▼
         Generated Answer
                 |
                 ▼
       Answer + Source URLs
                 |
                 ▼
          Gradio Interface
```

## 📂 Project Structure

```text
Eleven-Madison-Park-AI/
│
├── app.py                          # Gradio application
├── config.py                       # Configuration settings
├── ingestion.py                    # Document loading and splitting
├── embeddings.py                   # Gemini embedding initialization
├── vector_store.py                 # ChromaDB initialization and persistence
├── rag_chain.py                    # RAG pipeline implementation
│
├── eleven_madison_park_data.txt    # Collected website content
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template
├── .gitignore                      # Git ignored files
└── README.md                       # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Shreyansh1337/Eleven-Madison-Park-AI.git
```

Navigate to the project directory:

```bash
cd Eleven-Madison-Park-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Get a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project's root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Important:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
python app.py
```

The application will initialize the vector database and launch the Gradio interface.

Open the local URL displayed in your terminal, usually:

```text
http://127.0.0.1:7860
```

## 🔍 How It Works

The application consists of two main stages.

### Stage 1: Document Ingestion and Indexing

1. Website content is loaded from the collected text dataset.
2. Documents are separated and split into smaller chunks.
3. Gemini's embedding model converts each chunk into a numerical vector.
4. The resulting embeddings are stored in ChromaDB.
5. The vector database persists locally so embeddings can be reused across application restarts.

### Stage 2: Retrieval and Answer Generation

1. The user submits a natural-language question through Gradio.
2. LangChain sends the question to the retriever.
3. ChromaDB performs semantic similarity search.
4. The three most relevant document chunks are retrieved.
5. The retrieved context and user question are passed to Google Gemini.
6. Gemini generates a response based on the retrieved information.
7. The answer and corresponding source URLs are displayed in the interface.

## ⚙️ Configuration

The main configuration parameters are maintained in `config.py`.

| Parameter            | Value                   |
| -------------------- | ----------------------- |
| Embedding Model      | `gemini-embedding-001`  |
| Embedding Dimensions | 768                     |
| LLM                  | `gemini-3.1-flash-lite` |
| Temperature          | 0                       |
| Chunk Size           | 750                     |
| Chunk Overlap        | 150                     |
| Retrieval Top-K      | 3                       |
| Vector Database      | ChromaDB                |

## 🚀 Future Improvements

Potential enhancements for future versions:

- Conversational memory for follow-up questions.
- Improved retrieval using metadata filtering and reranking.
- RAG evaluation to measure retrieval relevance and answer quality.
- More detailed source citations with retrieved text passages.
- Cloud deployment for public access.
- Improved user interface and conversation history.

## ⚠️ Limitations

- Answers depend on the information available in the collected website dataset.
- Information may become outdated if the source content changes.
- The application requires a valid Google Gemini API key.
- Answer quality depends on retrieval relevance and the completeness of the available context.

## 👨‍💻 Author

**Shreyansh**

GitHub: [@Shreyansh1337](https://github.com/Shreyansh1337)

---


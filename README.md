# 🤖 RAG Chatbot using LangChain, OpenAI & ChromaDB

> **A Retrieval-Augmented Generation (RAG) chatbot that answers user questions using information retrieved from custom documents. Built with LangChain, OpenAI, ChromaDB, and Python.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![RAG](https://img.shields.io/badge/Architecture-RAG-red)

---

# 🏗 Solution Architecture

```text
                    User Question
                         │
                         ▼
                  Retrieval Pipeline
                         │
                         ▼
                ChromaDB Vector Store
                         │
                  Similarity Search
                         │
                         ▼
             Relevant Document Chunks
                         │
                         ▼
                GPT-4o (OpenAI LLM)
                         │
                         ▼
                 AI Generated Answer
```

---

# 🔄 RAG Workflow

```text
                 Text Documents
                        │
                        ▼
              Directory Loader
                        │
                        ▼
               Text Splitting
                        │
                        ▼
            OpenAI Embeddings
                        │
                        ▼
              ChromaDB Storage
                        │
                        ▼
                User Question
                        │
                        ▼
            Similarity Search (Top-K)
                        │
                        ▼
            Relevant Context Retrieved
                        │
                        ▼
                  GPT-4o Response
```

---

# 📂 Project Structure

```text
RAG-Chatbot/
│
├── Documents/
│     └── *.txt
│
├── db/
│     └── chroma_db/
│
├── 1_ingestion_pipeline.py
├── 2_Retrieval_pipeline.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🚀 Features

* Load multiple text documents automatically
* Split documents into manageable chunks
* Generate embeddings using OpenAI Embeddings
* Store embeddings in ChromaDB
* Perform semantic similarity search
* Retrieve the most relevant document chunks
* Generate context-aware responses using GPT-4o
* Interactive command-line chatbot
* Persistent vector database

---

# ⚙ Technologies Used

* Python
* LangChain
* OpenAI GPT-4o
* OpenAI Embeddings (text-embedding-3-small)
* ChromaDB
* CharacterTextSplitter
* DirectoryLoader
* dotenv

---

# 📚 How It Works

## Step 1 – Document Ingestion

* Load all `.txt` files from the **Documents** folder.
* Validate that documents are available.

---

## Step 2 – Text Chunking

* Split documents into chunks.
* Chunk Size: **1000**
* Chunk Overlap: **0**

---

## Step 3 – Embedding Generation

* Generate vector embeddings using:

```
text-embedding-3-small
```

---

## Step 4 – Vector Database

* Store embeddings in ChromaDB.
* Persist vectors locally for future retrieval.

---

## Step 5 – Retrieval

When a user asks a question:

1. Convert the question into an embedding.
2. Search ChromaDB.
3. Retrieve the Top-3 most relevant chunks.
4. Build context.
5. Send context + question to GPT-4o.
6. Generate the final answer.

---

# ▶ Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

---

## Run Ingestion

```bash
python 1_ingestion_pipeline.py
```

---

## Start Chatbot

```bash
python 2_Retrieval_pipeline.py
```

---

# 📸 Screenshots

## Document Ingestion

> *(Add Screenshot)*

---

## Chunk Creation

> *(Add Screenshot)*

---

## ChromaDB Creation

> *(Add Screenshot)*

---

## Question Answering

> *(Add Screenshot)*

---

# 📈 Current Features

| Module                  | Status |
| ----------------------- | ------ |
| Document Loading        | ✅      |
| Text Chunking           | ✅      |
| OpenAI Embeddings       | ✅      |
| ChromaDB                | ✅      |
| Semantic Search         | ✅      |
| Retrieval Pipeline      | ✅      |
| GPT-4o Integration      | ✅      |
| Interactive Chat        | ✅      |
| Persistent Vector Store | ✅      |

---

# 🎯 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* LangChain
* Vector Databases
* ChromaDB
* OpenAI API Integration
* Embedding Models
* Semantic Search
* Prompt Engineering
* Context Retrieval
* Python Programming

---

# 📖 Learning Outcomes

This project demonstrates:

* Building a complete RAG pipeline
* Document ingestion and preprocessing
* Text chunking strategies
* Embedding generation
* Vector database implementation
* Semantic retrieval
* LLM-powered question answering
* Persistent vector storage with ChromaDB

---

# 🚀 Future Enhancements

## Version 1.1

* PDF Document Loader
* DOCX Support
* Multiple File Formats

---

## Version 1.2

* Streamlit UI
* Chat Interface
* Upload Documents

---

## Version 2.0

* Conversation Memory
* Query Rewriting
* Hybrid Search
* Metadata Filtering

---

## Version 3.0

* Multi-Document Collections
* Citation Support
* Source Highlighting
* Evaluation Metrics

---

# 📄 License

This project is intended for learning, experimentation, demonstration, and portfolio purposes.

---

⭐ If you found this project useful, feel free to fork it and build upon it.

Developed with ❤️ using Python, LangChain, OpenAI, and ChromaDB.

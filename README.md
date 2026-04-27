🤖 Intelligent RAG Chatbot using LangChain & Transformers
📌 Overview

This project is an Intelligent Document-Based Chatbot built using Retrieval-Augmented Generation (RAG). It allows users to upload or load documents and ask natural language questions. The system retrieves relevant context using vector similarity search and generates accurate answers using transformer-based models.

🚀 Features
📄 Document-based Question Answering (PDF support)
🔍 Semantic search using embeddings
🧠 RAG pipeline with LangChain
🤖 Transformer-based LLM (HuggingFace)
📚 FAISS vector database for fast retrieval
💬 Chat-style Streamlit UI
📄 Source document display for transparency
🛠️ Tech Stack
Python 🐍
LangChain 🦜
HuggingFace Transformers 🤗
SentenceTransformers
FAISS (Vector Database)
Streamlit (Frontend UI)
🏗️ Architecture
User Question
     ↓
Streamlit UI
     ↓
LangChain RAG Chain
     ↓
FAISS Vector Search (Embeddings)
     ↓
Relevant Document Chunks
     ↓
Transformer Model (FLAN-T5)
     ↓
Final Answer + Sources
📁 Project Structure
rag-chatbot/
│
├── data/                  # PDF documents
├── src/
│   ├── loader.py         # Load PDF files
│   ├── splitter.py       # Split text into chunks
│   ├── embeddings.py     # Generate embeddings
│   ├── vectorstore.py    # FAISS vector DB
│   ├── rag_chain.py      # RAG pipeline
│
├── app.py                # Streamlit chatbot UI
├── requirements.txt      # Dependencies
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
streamlit run app.py

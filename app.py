import streamlit as st
from src.loader import load_docs
from src.splitter import split_docs
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore
from src.rag_chain import build_rag_chain

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("🤖 Intelligent RAG Chatbot")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# setup pipeline
@st.cache_resource
def setup():
    docs = load_docs("data/ML_Introduction.pdf")
    split = split_docs(docs)
    emb = get_embeddings()
    vs = create_vectorstore(split, emb)
    return build_rag_chain(vs)

qa_chain = setup()

# display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

query = st.chat_input("Ask a question...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    with st.spinner("Thinking..."):
        result = qa_chain({"query": query})
        answer = result["result"]
        sources = result["source_documents"]

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)

    with st.expander("📄 Source Documents"):
        for i, doc in enumerate(sources):
            st.write(f"Source {i+1}")
            st.write(doc.page_content[:200] + "...")
            st.write("---")
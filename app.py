import streamlit as st
from src.pdf_loader import load_pdf
from src.text_splitter import split_text
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.llm_handler import get_llm, generate_answer
import base64
import time

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Theme toggle
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

with st.sidebar:
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown("### 🌗 Theme")
    with col2:
        light_mode = st.toggle("🌞", value=False)

    st.session_state.theme = "light" if light_mode else "dark"


if st.session_state.theme == "light":
    st.markdown("""
        <style>
        .stApp {
            background-color: #F5F5F5;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

st.title("🤖 AI Document Assistant")
st.caption("Upload PDFs and chat with your documents using AI")


# -------------------------------
# Sidebar
# -------------------------------


with st.sidebar:
    st.divider()
    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf", "docx", "txt", "csv"],
        accept_multiple_files=True
    )

    st.divider()

    st.markdown("### ℹ️ About")
    st.write(
        """
        This AI assistant uses **RAG (Retrieval Augmented Generation)** to answer questions from uploaded documents.
        
        **Tech Stack**
        - Streamlit
        - LangChain
        - FAISS Vector DB
        - Sentence Transformers
        - Groq Llama-3
        """
    )
# -------------------------------
#  Doc Preview
# -------------------------------
# if uploaded_files:

#     st.subheader("📄 Document Preview")

#     preview_file = uploaded_files[0]

#     pdf_bytes = preview_file.read()
#     base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

#     pdf_display = f"""
#         <iframe 
#         src="data:application/pdf;base64,{base64_pdf}" 
#         width="100%" 
#         height="600"
#         type="application/pdf">
#         </iframe>
#     """

#     st.markdown(pdf_display, unsafe_allow_html=True)
if uploaded_files:
    st.subheader("📄 Uploaded Documents:")
    for file in uploaded_files:
        st.write(f"• {file.name}")
# -------------------------------
# Cache models
# -------------------------------

@st.cache_resource
def load_embeddings():
    return get_embedding_model()


@st.cache_resource
def load_llm():
    return get_llm()

@st.cache_resource
def build_vector_store(chunks, _embedding_model):
    return create_vector_store(chunks, _embedding_model)

# -------------------------------
# Session State
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "llm" not in st.session_state:
    st.session_state.llm = None


# -------------------------------
# Process PDFs
# -------------------------------
if "uploaded_file_names" not in st.session_state:
    st.session_state.uploaded_file_names = []
current_files = [file.name for file in uploaded_files] if uploaded_files else []

if current_files != st.session_state.uploaded_file_names:
    st.session_state.uploaded_file_names = current_files
    st.session_state.vector_store = None
    st.session_state.messages = []
 
if uploaded_files and st.session_state.vector_store is None:

    with st.spinner("📚 Processing documents..."):

        documents = []
        for file in uploaded_files:
            docs = load_pdf(file)
            documents.extend(docs)
        chunks = split_text(documents)
        embedding_model = load_embeddings()
        # vector_store = create_vector_store(chunks, embedding_model)
        vector_store = build_vector_store(chunks, embedding_model)

        llm = load_llm()

        st.session_state.vector_store = vector_store
        st.session_state.llm = llm

    st.success("Documents processed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Documents Uploaded", len(uploaded_files))

    with col2:
        st.metric("Text Chunks Created", len(chunks))


# -------------------------------
# Display Chat History
# -------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# -------------------------------
# Chat Input
# -------------------------------

question = st.chat_input("Ask a question about your documents")


if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    if st.session_state.vector_store is None:
        st.warning("Please upload documents first.")

    else:

        vector_store = st.session_state.vector_store
        llm = st.session_state.llm

        with st.spinner("🤖 Thinking..."):

            docs = retrieve_documents(vector_store, question)

            answer = generate_answer(llm, docs, question)

        # with st.chat_message("assistant"):
        #     st.write(answer)

        # with st.chat_message("assistant"):

        #     message_placeholder = st.empty()
        #     full_response = ""

        #     for word in answer.split():
        #         full_response += word + " "
        #         message_placeholder.markdown(full_response)
        #         time.sleep(0.03)
        with st.chat_message("assistant"):

            message_placeholder = st.empty()
            full_response = ""

            for char in answer:
                full_response += char
                message_placeholder.markdown(full_response)
                time.sleep(0.01)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        # Show sources
        with st.expander("📄 Source Context"):
            for doc in docs:
                st.write(f"**Page {doc.metadata.get('page')}**")
                st.write(doc.page_content)
                st.divider()
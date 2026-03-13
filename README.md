# 🤖 AI Document Assistant (RAG)

An AI-powered **Document Question Answering System** that allows users to upload documents and ask questions about their content using **Retrieval Augmented Generation (RAG)**.

The system retrieves relevant document sections using **vector similarity search** and generates answers using **Llama 3.1 via Groq API**.

---

## 🚀 Features

* 📂 Upload and chat with your documents
* 📑 Supports multiple file types

  * PDF
  * DOCX
  * TXT
  * CSV
* 🔎 Semantic search using **FAISS vector database**
* 🧠 Context-aware answers using **RAG architecture**
* ⚡ Fast responses using **Groq Llama-3.1 model**
* 💬 ChatGPT-style conversational interface
* 🌗 Dark / Light theme toggle
* 📌 Source citations with page numbers
* ⚡ Streaming AI responses (typing effect)

---

## 🧠 Architecture

```
User Uploads Documents
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Database
        ↓
User Question
        ↓
Vector Similarity Search
        ↓
Relevant Context Retrieved
        ↓
LLM (Llama 3.1 via Groq)
        ↓
AI Generated Answer
```

---

## 🛠 Tech Stack

* **Python**
* **Streamlit** – Web interface
* **LangChain** – LLM orchestration
* **FAISS** – Vector database
* **Sentence Transformers** – Embedding model
* **Groq API** – Llama-3.1 inference
* **PyPDF / python-docx / pandas** – Document parsing

---

## 📂 Project Structure

```
rag-document-qa
│
├── app.py
├── requirements.txt
├── README.md
│
├── src
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── llm_handler.py
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/0hhh/rag-document-qa.git
cd rag-document-qa
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add API key

Create `.env`

```
GROQ_API_KEY=your_groq_api_key
```

---

### 5️⃣ Run the app

```
streamlit run app.py
```

---

## 🌐 Deployment

This project can be deployed easily using **Streamlit Community Cloud**.

Steps:

1. Push the project to **GitHub**
2. Go to **Streamlit Cloud**
3. Connect your GitHub repository
4. Deploy using:

```
app.py
```

---

## 📸 Example Use Cases

* Ask questions about **research papers**
* Analyze **financial reports**
* Extract insights from **company documents**
* Chat with **internal knowledge bases**

---

## 🔮 Future Improvements

* Hybrid search (Vector + Keyword)
* Answer confidence scoring
* Document highlighting
* Chat history export
* Docker deployment
* Multi-user support

---

## 👨‍💻 Author

Built as an **AI portfolio project** demonstrating practical use of:

* Retrieval Augmented Generation (RAG)
* Vector databases
* LLM-powered applications

---

## ⭐ If you found this useful

Give the repo a ⭐ on GitHub!

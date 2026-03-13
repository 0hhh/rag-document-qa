import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# def get_llm():
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
#     return client
def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key and "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]

    client = Groq(api_key=api_key)

    return client


# def generate_answer(llm, docs, question):

#     context = "\n\n".join([doc.page_content for doc in docs])

#     prompt = f"""
# Answer the question using ONLY the context below.

# Context:
# {context}

# Question:
# {question}
# """

#     completion = llm.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3
#     )

#     return completion.choices[0].message.content

def generate_answer(llm, docs, question):

    context = "\n\n".join(
        [
            f"(File: {doc.metadata.get('source')} Page {doc.metadata.get('page')}) {doc.page_content}"
            for doc in docs
        ]
    )
    # context = "\n\n".join([doc.page_content[:500] for doc in docs])
    
    prompt = f"""
You are an assistant answering questions from documents.

Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and cite the page numbers if possible.
"""

    completion = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )


    return completion.choices[0].message.content

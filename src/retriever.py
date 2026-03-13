from langchain_core.documents import Document

def retrieve_documents(vector_store, query):

    docs = vector_store.similarity_search(
        query,
        k=5
    )

    return docs
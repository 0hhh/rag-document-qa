# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        # model_name="sentence-transformers/all-MiniLM-L6-v2"
         model_name="sentence-transformers/all-mpnet-base-v2"   
    )

    return embedding_model
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def split_text(text):

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100
#     )

#     chunks = splitter.split_text(text)

#     return chunks

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks
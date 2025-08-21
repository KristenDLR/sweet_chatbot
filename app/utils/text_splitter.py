from langchain.text_splitter import RecursiveCharacterTextSplitter

# Splits LangChain documents into smaller chunks for embeddings.
def split_documents(documents, chunk_size=800, chunk_overlap=100):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""], 
    )
    return splitter.split_documents(documents)

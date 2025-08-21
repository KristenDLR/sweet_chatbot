from langchain.schema import Document
from utils.text_splitter import split_documents

# Use an example of a fake document
docs = [Document(page_content="This is a long text. " * 50)]

chunks = split_documents(docs, chunk_size=100, chunk_overlap=20)

print(f"Original text length: {len(docs[0].page_content)}")
print(f"Number of chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---\n{chunk.page_content}")

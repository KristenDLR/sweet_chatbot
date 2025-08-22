import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def embed_chunks(chunks: list[str]):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=openai_api_key
    )
    vectors = embeddings.embed_documents(chunks)
    return vectors

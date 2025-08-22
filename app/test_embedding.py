from services.embedding_service import embed_chunks

if __name__ == "__main__":
    chunks = [
        "The Eiffel Tower is in Paris.",
        "FastAPI is a Python framework for building APIs.",
        "ChromaDB stores embeddings for retrieval."
    ]

    vectors = embed_chunks(chunks)

    print(f"Number of vectors: {len(vectors)}")
    print(f"Length of each vector: {len(vectors[0])}")
    print("First vector snippet:", vectors[0][:10])  # preview first 10 numbers

from .pdf_loader import load_pdf

__all__ = ["load_pdf"]

# Local test/example usage
if __name__ == "__main__":
    from langchain_community.document_loaders import PyPDFLoader
    
    # TODO: In production, store the PDF URL in .env and host the file.
    # Then download temporarily and load with PyPDFLoader.
    file_path = "backend/data/Nestle_Dataset.pdf"  # adjust if needed
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages")
    print(documents[0].page_content[:300])  # preview first 300 characters

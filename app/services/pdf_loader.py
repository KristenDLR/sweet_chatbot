from langchain_community.document_loaders import PyPDFLoader

# TODO: Production, store the URL in .env and PDF needs to be hosted, download it temporarily and then load it with PyPDFLoader
def load_pdf(file_path: str):
    file_path = "data/Nestle_Dataset.pdf"
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages")
    return documents

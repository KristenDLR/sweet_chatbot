
if __name__ == "__main__":
    from langchain_community.document_loaders import PyPDFLoader
    
    file_path = "data/Nestle_Dataset.pdf" 
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages")
    print(documents[0].page_content[:300]) 

import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Set up paths
docs_dir = "docs"
db_path = "crypto_forge_kb"

# Load and split documents
documents = []
for file in os.listdir(docs_dir):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(docs_dir, file))
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = splitter.split_documents(docs)
        documents.extend(split_docs)

# Embeddings (use GPU if CUDA True)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
)

# Create and save FAISS index
db = FAISS.from_documents(documents, embeddings)
db.save_local(db_path)
print(f"Knowledge base created at {db_path} with {len(documents)} chunks.")

# Test Query Function
def test_kb_query(query):
    results = db.similarity_search(query, k=3)
    for res in results:
        print(f"Relevant Chunk: {res.page_content[:200]}... (Source: {res.metadata['source']})")

if __name__ == "__main__":
    test_kb_query("secure element for Bitcoin wallets")

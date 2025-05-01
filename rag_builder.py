# rag_builder.py

import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the PDF syllabus
pdf_path = "MTech-CSE-_Curriculum_Syllabus_2022.pdf"  # Update path if needed
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Split text into chunks for better retrieval
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " "]
)
chunks = splitter.split_documents(documents)

# Create embeddings using a lightweight SentenceTransformer model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create a vector store (Chroma)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./course_index"
)

# Save the vector store locally
vectorstore.persist()

print(f"✅ Vector store built and saved to './course_index' with {len(chunks)} chunks.")

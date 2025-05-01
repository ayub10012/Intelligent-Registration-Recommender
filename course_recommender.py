import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import PyPDFLoader

load_dotenv()

# Load the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Load Chroma vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./course_index", embedding_function=embedding_model)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# --- Streamlit UI ---
st.set_page_config(page_title="Course Recommender", layout="wide")
st.title("Course Recommendation Based on Grades + Interests")

# File Upload
grade_file = st.file_uploader(" Upload your grade sheet (PDF, TXT, or CSV)", type=["pdf", "txt", "csv"])
query = st.text_area(" Describe your interests, goals, or career path:")

grade_text = ""

# Handle different file types
if grade_file:
    ext = grade_file.name.split(".")[-1]
    if ext == "pdf":
        with open("temp_grade_sheet.pdf", "wb") as f:
            f.write(grade_file.read())
        loader = PyPDFLoader("temp_grade_sheet.pdf")
        documents = loader.load()
        grade_text = "\n".join([doc.page_content for doc in documents])
    elif ext == "txt":
        grade_text = grade_file.read().decode("utf-8")
    elif ext == "csv":
        df = pd.read_csv(grade_file)
        grade_text = df.to_string(index=False)

    st.subheader("Parsed Grade Sheet")
    st.text_area("Check the extracted content from your grade file:", grade_text, height=200)

# Run Recommendation
if st.button(" Recommend Courses"):
    if not grade_text.strip():
        st.warning("Please upload your grade sheet.")
    else:
        full_prompt = f"""I am a student seeking course recommendations, proper explinations,don't give exist completed course in the grade sheet, recommend all related course
        

My past academic performance is as follows:
{grade_text}

My personal interests and career goals are:
{query if query else 'Not provided'}

Based on the above, suggest suitable courses from the syllabus."""
        with st.spinner("Thinking..."):
            result = rag_chain({"query": full_prompt})
            st.subheader("Recommended Courses")
            st.write(result["result"])

            st.subheader(" Source Snippets")
            for doc in result["source_documents"]:
                st.markdown("---")
                st.markdown(doc.page_content[:500] + ("..." if len(doc.page_content) > 500 else ""))

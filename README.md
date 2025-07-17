🧠 Intelligent Registration Recommender (IRR)
Personalized course recommendation system powered by LLMs and RAG for VIT students.

📌 Project Overview
The Intelligent Registration Recommender (IRR) is an AI-powered system that provides personalized course recommendations to students based on their academic curriculum, completed courses, previous grades, institutional constraints, and personal preferences.

Built using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) techniques, the system helps streamline semester course planning and enables smarter decision-making for students.

🎯 Objectives
Analyze students' academic history and curriculum structure.

Generate relevant SQL queries dynamically via LLMs.

Recommend courses that align with academic goals and personal interests.

Deliver results through an intuitive frontend using Streamlit.

| Component            | Technology            |
| -------------------- | --------------------- |
| Language Model       | Gemini 2.0 Flash API  |
| Orchestration        | LangChain + LangGraph |
| Database             | MySQL (`vit_courses`) |
| Frontend             | Streamlit             |
| Programming Language | Python                |

🧩 System Architecture
📦 Modules Implemented
Natural Language Processing Module

Utilizes Gemini model for semantic understanding of student queries.

SQL Query Generation

Converts interpreted intent into dynamic SQL queries using LangChain's SQL toolkit.

Response Formatting

Neatly presents results in user-readable format.

LangGraph Agent

Manages reasoning flow and orchestrates tool usage.

🗄️ Database Schema
Database Name: vit_courses
Table: courses

| Column       | Description              |
| ------------ | ------------------------ |
| course\_code | Unique identifier        |
| course\_name | Name of the course       |
| credits      | Credit value             |
| department   | Department offering it   |
| category     | Course category          |
| course\_type | Type (core/elective etc) |


🧠 Agent Prompt Highlights
Understand user's natural language query.

Identify course-related entities (type, category, keywords).

Generate SQL dynamically.

Execute via LangChain tools.

Format and return results cleanly.

📝 NLP-to-SQL Pseudocode
Input: User Query
↓
Tokenize → Extract keywords
↓
Identify course_type / category
↓
Construct SQL:
SELECT course_code, course_name ...
FROM courses
WHERE course_name LIKE '%keyword%'
↓
Execute using SQLDatabaseTool
↓
Return Results


⚠️ Challenges
Handling ambiguous or multi-intent queries.

Ensuring semantic accuracy in SQL generation.

🚀 Future Improvements
Add fuzzy keyword matching for broader search capability.

Extend to support multiple institutional databases.

Introduce feedback loop to learn from user choices.

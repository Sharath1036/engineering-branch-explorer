import streamlit as st
import langchain_model

st.title("Engineering Branch Overview: Salary, Syllabus")

branches = ["Choose a branch"] + sorted(["Computer", "Information Technology", "Data Science", "Electronics and Telecommunication", "Electronics and Computer Science", "Electronics", "Artificial Intelligence", "Artificial Intelligence and Data Science", "Artificial Intelligence and Machine Learning", "IoT, Blockchain and Cyber Security", "Mechanical", "Civil", "Chemical", "Electrical", "Biotechnology", "Biomedical", "Computer Science and Design", "Computer Science and Business Systems", "Production", "Textile"])


branch = st.sidebar.selectbox("Select a branch", branches)

if branch != "Choose a branch":
    response = langchain_model.branch_overview(branch)

    st.header("Salary")
    st.write(response['stream'].strip())

    st.header("Syllabus")
    st.write(response['syllabus'].strip())

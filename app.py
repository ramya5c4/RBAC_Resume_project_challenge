import streamlit as st
import requests
import re
from requests.auth import HTTPBasicAuth
from retrieval import load_data,retrieval_chain
st.title("💬 Chatbot for Role-based access control with RAG")
st.sidebar.header("Login")
username = st.sidebar.text_input("Username", value="")
password = st.sidebar.text_input("Password", type="password", value="")
if st.sidebar.button("Login"):
     try:
       res = requests.get("http://localhost:8000/login",auth=HTTPBasicAuth(username, password))
       res.raise_for_status()
       st.session_state.auth = (username, password)
       st.sidebar.write("Login successfully")
     except Exception as e:
        st.error("Login failed. Check credentials.")



if "auth" in st.session_state:
   res1 = requests.get("http://localhost:8000/test",auth=HTTPBasicAuth(*st.session_state.auth))
   chat_msg=res1.json()
   with st.chat_message("assistant"):
           st.write(chat_msg['message'])
           st.write(f"Role : {chat_msg['role']}")
   question=st.chat_input("",key="chat_input")
   if question:
        with st.chat_message("user"):
            st.write(question)
        load_data(chat_msg["role"])
        chain=retrieval_chain()
        answer=chain(question)
        result=answer["result"]
        answers = re.sub(r'^#+\s*|\d+\.*\s*', '', result)
        with st.chat_message("assistant"):
              st.write(answers)




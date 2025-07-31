import requests
import streamlit as st

def get_groq_response(req):
    response = requests.post("http://localhost:8000/poem2", json={"prompt": req})
    return response.json()['response']

def get_groq_essay(req):
    response=requests.post("http://localhost:8000/essay",
    json={'topic':req})
    return response.json()['response']

st.title("Langchain api")
input_text=st.text_input("write your query")
input_text1=st.text_input("write your topic for essay")

if input_text:
    st.write(get_groq_response(input_text))

if input_text1:
    st.write(get_groq_essay(input_text1))


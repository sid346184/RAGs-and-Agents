from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please provide relevant response to the user queries"),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("Langchain Chatbot")
input_text = st.text_input("Enter your question")

# LLM
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

# Output parser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Run chain
if input_text:
    result = chain.invoke({"question": input_text})
    st.write(result)

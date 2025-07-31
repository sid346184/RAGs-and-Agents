from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

app=FastAPI(
    title='Langchain Server',
    version='1.0',
    description='api server'
)

output=StrOutputParser()

add_routes(
    app,
    ChatGroq(model="llama3-8b-8192"),
    path="/groq"
)

model1=ChatGroq(model="llama3-8b-8192")
model2=ChatGroq(model="llama3-8b-8192")
prompt1=ChatPromptTemplate.from_template("Write Essay about {topic} in about 100 words")
prompt2=ChatPromptTemplate.from_template("Write poem about {topic} in about 100 words") 

@app.post("/essay")
async def generate_essay(data: dict):
    topic = data.get("topic")
    chain = prompt1 | model1 | output
    return {"response": chain.invoke({"topic": topic})}


@app.post("/poem")
async def generate_(data: dict):
    topic = data.get("topic")
    chain = prompt2 | model2 | output
    return {"response": chain.invoke({"topic": topic})}

@app.post("/poem2")
async def generate_(data: dict):
    topic = data.get("topic")
    chain = prompt2 | model2 | output
    return {"response": chain.invoke({"topic": topic})}

if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port=8000)
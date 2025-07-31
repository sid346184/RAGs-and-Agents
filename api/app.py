from fastapi import FastAPI
from pydantic import BaseModel
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='API Server'
)

output = StrOutputParser()
model1 = ChatGroq(model="llama3-8b-8192")
model2 = ChatGroq(model="llama3-8b-8192")

prompt1 = ChatPromptTemplate.from_template("Write Essay about {topic} in about 100 words")
prompt2 = ChatPromptTemplate.from_template("Write poem about {topic} in about 100 words")

class TopicRequest(BaseModel):
    topic: str

@app.post("/essay")
async def generate_essay(data: TopicRequest):
    chain = prompt1 | model1 | output
    return {"response": chain.invoke({"topic": data.topic})}

@app.post("/poem")
async def generate_poem(data: TopicRequest):
    chain = prompt2 | model2 | output
    return {"response": chain.invoke({"topic": data.topic})}

class PromptRequest(BaseModel):
    prompt: str

@app.post("/groq")
async def run_groq(request: PromptRequest):
    model = ChatGroq(model="llama3-8b-8192")
    chain=model|output
    return {"response": model.invoke(request.prompt)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

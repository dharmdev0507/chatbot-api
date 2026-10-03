import os
import uvicorn
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from dotenv import load_dotenv
#from ollama_llm import llm
from groq_llm import llm

#load environment variable
load_dotenv()
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']="true"

#Fast API 
api=FastAPI(
    title='Fast API',
    version='1.0',
    description='This is chatbot app'
)

#prompts
prompt=ChatPromptTemplate.from_template('{prompts}')

add_routes(
    api,
    prompt|llm,
    path='/chat'
)

#to start python using 
if __name__=='__main__':
    uvicorn.run(api,host='localhost',port=8500)
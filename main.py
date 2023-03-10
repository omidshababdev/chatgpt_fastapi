import openai
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Union

load_dotenv()
app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "text-davinci-003"

def chatgpt(prompt):
  completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    n = 1,
    temperature = 0.5
  )
  response = completion.choices[0].text
  return f"ChatGPT: {response}"

class Prompt(BaseModel):
    prompt: Union[str, None] = None

@app.get("/")
async def root():
    return {"message": "Welcome to ChatGPT FastAPI"}
  
@app.post("/")
async def hello(prompt: Prompt):
    try:
      return {"ChatGPT": chatgpt(prompt)}
    except NameError:
      return {"Error": NameError}
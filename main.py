from fastapi import FastAPI
import os
import google.genai as genai

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/")
def root():
    return {"message": "Hello Skynet"}

@app.get("/ask")
def ask(q: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=q
    )
    return {"reply": response.text}

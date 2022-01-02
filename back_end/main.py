from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from load_model import getanswer

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
context = "The US has passed the peak on new coronavirus cases, " \
          "President Donald Trump said and predicted that some states would reopen this month. " \
          "The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world."
@app.get("/")
def sum(question):
    ans = getanswer(question, context)
    return {"answer": ans['answer']}

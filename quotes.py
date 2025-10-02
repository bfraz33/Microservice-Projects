from fastapi import FastAPI
import random

app = FastAPI()

QUOTES = [
        "I have a dream. - Martin Luther King Jr."
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
        "The way to get started is to quit talking and begin doing.  - Walt Disney"
        "To be, or not to be, that is the question.  - William Shakespeare"
        "A journey of a thousand miles begins with a single step.  - Lao Tzu"
]

@app.get("/quotes")
def get_quotes(quotes):
    return {"Quotes:" : random.choice(QUOTES)}
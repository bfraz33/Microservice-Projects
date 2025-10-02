from fastapi import FastAPI
import random

app = FastAPI()

ALWC = {
    "Yankees": "American League Wild Card",
    "Red Sox": "American League Wild Card",
    "Guardians": "American League Wild Card",
    "Tigers": "American League Wild Card",
    "Blue Jays": "American League Wild Card",
    "Mariners": "American League Wild Card"

}


NLWC = {
    "Dodgers": "National League Wild Card",
    "Reds": "National League Wild Card",
    "Cubs": "National League Wild Card",
    "Padres": "National League Wild Card",
    "Brewers": "National League Wild Card",
    "Phillies": "National League Wild Card"
}

@app.get("/ALWC")
def get_alwc():
    return {"ALWC Teams": list(ALWC.keys())}

@app.get("/NLWC")
def get_nlwc():
    return{"NLWC Teams": list(NLWC.keys())}
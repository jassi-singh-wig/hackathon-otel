from typing import Union
import requests
from fastapi import FastAPI
import time
from random import randint

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World FastAPI 2"}


@app.get("/square-v1/{number}")
def fetch_from_app1(number: int):
    response = requests.post(url="http://fast-app1:5001/squarefromapp1/" + str(number))
    return {"Square value": response.text}

@app.get("/square-v2/{number}")
def fetch_from_app1(number: int):
    time.sleep(randint(1, 6))
    response = requests.post(url="http://fast-app1:5001/squarefromapp1/" + str(number))
    return {"Square value": response.text}

@app.get("/square-v3/{number}")
def fetch_from_app1(number: int):
    response = requests.post(url="http://fast-app1:5001/squarefromapp1",data=number)
    return {"Square value": response.text}
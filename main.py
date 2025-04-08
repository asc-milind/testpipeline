# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    "test"
    return {"message": "Testing Workflow 10"}


@app.get("/a")
def read_root_a():
    return {"message": "Testing Workflow 10"}

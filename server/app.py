from fastapi import FastAPI
from inference import run_demo

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Workplace Decision Engine Running"}

@app.get("/run-demo")
def demo():
    return run_demo()
from fastapi import FastAPI

app = FastAPI(title="Lucky")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def read_name():
    return {"name": "lakshmi"}

@app.get("/batch")
def read_batch():
    return {"batch": "Batch 55B"}
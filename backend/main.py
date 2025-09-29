
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "speedaf-api"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/hello")
def hello():
    return {"msg": "Hello Speedaf"}

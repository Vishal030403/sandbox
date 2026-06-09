from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}!"}
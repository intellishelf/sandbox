import json
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
        "http://localhost",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)
@app.get("/")
async def root():
     with open('books.json', 'r') as f:
        data = json.load(f)
        return data



@app.post("/books")
async def books(index: int = None):
     with open('books.json', 'r') as f:
        data = json.load(f)
        if index is not None:
            return data[index]
        return data
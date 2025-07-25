from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from retrival import build_rag_chain

app = FastAPI()
rag_chain = build_rag_chain()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/generate")
def generate_answer(req: QueryRequest):
    result = rag_chain(req.query)
    return {"result": result["result"]}

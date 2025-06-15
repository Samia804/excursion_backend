'''# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class Trip(BaseModel):
    tripTitle: str
    destination: str
    pricePerSeat: str
    startDate: str
    endDate: str

class ChatResponse(BaseModel):
    trips: List[Trip]

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    print("✅ Request received:", request.message)
    return ChatResponse(trips=[
        Trip(
            tripTitle="Sample Trip",
            destination="Swat",
            pricePerSeat="9999",
            startDate="2025-06-10",
            endDate="2025-06-15"
        )
    ])
@app.get("/")
def home():
    return {"message": "show me trips to sawat"}'''




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ChatRequest, ChatResponse
from langchain_utils import extract_trip_filters
from mongo_utils import search_trips

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://excursion-backend.onrender.com", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        print("📩 Received message:", request.message)
        filters = extract_trip_filters(request.message)
        trips = search_trips(filters)
        return ChatResponse(trips=trips)
    except Exception as e:
        print("💥 Chat endpoint crashed with error:", str(e))
        raise e

@app.get("/")
def home():
    return {"message": "Excursions API is live!"}

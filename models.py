from pydantic import BaseModel, Extra
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str

class Trip(BaseModel):
    tripTitle: str
    destination: str
    pricePerSeat: str
    startDate: str
    endDate: str
    companyName: Optional[str] = None
    tripImageUrl: Optional[str] = None

    class Config:
        extra = Extra.allow  # ✅ This fixes hanging issue

class ChatResponse(BaseModel):
    trips: List[Trip]

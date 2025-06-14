# mongo_utils.py
# 🌐 This connects to MongoDB Atlas and performs real trip filtering.

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# ✅ Load MongoDB URI from .env file
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
import os
print("🔗 Connecting with:", os.getenv("MONGO_URI"))


# ✅ Choose your database and collection
db = client["Excursions"]
collection = db["trips"]

def search_trips(filters):
    print("🔍 Searching Mongo with filters:", filters)

    # 🔎 Build MongoDB query using regex for destination and price filter
    query = {
        "destination": {"$regex": filters["destination"], "$options": "i"},
        "pricePerSeat": {"$lte": str(filters["max_price"])}  # stored as string in DB
    }

    # 🧾 Run the query
    result = collection.find(query)

    trips = []
    for doc in result:
        trips.append({
            "tripTitle": doc.get("tripTitle", ""),
            "destination": doc.get("destination", ""),
            "pricePerSeat": doc.get("pricePerSeat", ""),
            "startDate": doc.get("startDate", ""),
            "endDate": doc.get("endDate", ""),
            "companyName": doc.get("companyName", ""),
            "tripImageUrl": doc.get("tripImageUrl", "")
        })

    return trips

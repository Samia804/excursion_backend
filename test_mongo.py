import os
from pymongo import MongoClient
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# 🔗 Show the URI being used
mongo_uri = os.getenv("MONGO_URI")
print("🔗 Connecting with:", mongo_uri)

try:
    # ✅ Try to create client
    client = MongoClient(mongo_uri)
    print("✅ Connected to MongoDB client")

    # ✅ Try accessing the database
    db = client["Excursions"]
    print("📂 Accessed database: excursions")

    # ✅ Try accessing the collection
    trips = db["trips"]
    print("📄 Accessed collection: trips")

    # ✅ Fetch documents
    result = trips.find()
    trips_found = False
    for trip in result:
        print("📌 Trip found:", trip)
        trips_found = True

    if not trips_found:
        print("⚠️ No trips found in the collection.")

except Exception as e:
    print("❌ Error accessing trips collection:", e)





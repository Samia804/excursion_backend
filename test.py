# test_chat.py
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"message": "Show me Murree trips under 7000"}
)
print(response.status_code)
print(response.json())
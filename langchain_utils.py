# langchain_utils.py
from dotenv import load_dotenv
import os, json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI  # ✅ You’re using the right updated import


# ✅ Load .env for API key
load_dotenv()
print("🔑 Loaded key:", os.getenv("OPENAI_API_KEY"))

# ✅ Connect to ChatOpenAI with temperature=0 for consistency
llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# ✅ Friendly prompt for extracting filters
prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are Lara, a friendly, helpful travel assistant.

Understand the user's travel request and extract the following as a JSON:
- destination (string)
- max_price (number only)
- duration_days (number of days)
- trip_type (family, couple, friends, solo, etc.)

Only return valid JSON like this:
{{
    "destination": "Murree",
    "max_price": 5000,
    "duration_days": 3,
    "trip_type": "family"
}}

User message: {user_input}
"""
)


# ✅ LangChain chain
chain = LLMChain(llm=llm, prompt=prompt)

# ✅ Filter extraction function
def extract_trip_filters(user_input: str):
    print("📩 Got message:", user_input)

    response = chain.run(user_input=user_input)
    print("🧠 GPT raw output:\n", response)

    try:
        parsed = json.loads(response)
        print("✅ Parsed JSON:", parsed)
        return parsed
    except json.JSONDecodeError:
        print("❌ JSON parsing failed. Returning dummy filters.")
        return {
            "destination": "Murree",
            "max_price": 10000,
            "duration_days": 3,
            "trip_type": "family"
        }

# test_prompt.py
# Lets you test the LangChain prompt extraction before running the API

from langchain_utils import extract_trip_filters

result = extract_trip_filters("I want to go to Murree with family under 6000 for 3 days")
print(result)

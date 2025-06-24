#LIVE-RAG powered by SerpAPI 
#Built by Shabib

import os
from openai import OpenAI
import json
from serpapi import GoogleSearch
from dotenv import load_dotenv
load_dotenv()

system_prompt = """
You are a helpful assistant. Use the web search results provided to answer the user's query.
Do not guess. Use only the information from the search results.
At the end, include the sources (links) you used.
"""
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    { "role": "system", "content": system_prompt },
]

while True:
    user_input = input(">>")
    if user_input.lower() == "exit":
        break

    params = {
    "engine": "google",
    "q": user_input,
    "api_key": os.getenv("serpapi_key")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    if "organic_results" in results:
        search_context = ""
        sources = []
        for i, result in enumerate(results["organic_results"][:3]):
            title = result.get("title", "")
            link = result.get("link", "")
            snippet = result.get("snippet", "")
            search_context += f"{i+1}. {title}\n{snippet}\nSource: {link}\n\n"
            sources.append(link)
    else:
        search_context = "No results found."
        sources = []

    full_prompt = f"""User_Query: {user_input}\n\nHere are the Top Results\n\n{search_context}"""
    messages.append(
        {"role": "user", "content": full_prompt}
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    messages.append(
        {"role":"assistant","content": reply}
    )
    print("\n🤖 Assistant Response:\n")
    print(reply)
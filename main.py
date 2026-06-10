from fastapi import FastAPI
import random
import re

app = FastAPI(
    title="Bhagavad Gita Quotes API",
    description="Get random Bhagavad Gita quotes for motivation",
    version="1.0.0"
)

with open("bhagavad_gita_quotes.txt", "r", encoding="utf-8") as file:
    content = file.read()

quotes = re.findall(r'\d+\.\s+"([^"]+)"', content)

if not quotes:
    raise RuntimeError("No quotes found")

@app.get("/")
async def root():
    return {
        "message": "Bhagavad Gita Quotes API",
        "endpoint": "/api/v1/quotes/random"
    }

@app.get("/api/v1/quotes/random")
async def get_random_quote():
    return {
        "quote": random.choice(quotes)
    }
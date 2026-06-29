from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import re

app = FastAPI(
    title="gitaquotes API",
    description="Get random Bhagavad Gita quotes for motivation",
    version="1.0.0"
)

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("bhagavad_gita_quotes.txt", "r", encoding="utf-8") as file:
    content = file.read()

quotes = re.findall(r'\d+\.\s+"([^"]+)"', content)

if not quotes:
    raise RuntimeError("No quotes found")

@app.get("/")
async def root():
    return {
        "message": "gitaquotes API",
        "endpoint": "/api/v1/quotes/random"
    }

@app.get("/api/v1/quotes/random")
async def get_random_quote():
    return {
        "quote": random.choice(quotes)
    }
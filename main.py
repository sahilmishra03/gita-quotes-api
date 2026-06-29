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

import os

def load_quotes(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    return re.findall(r'\d+\.\s+"([^"]+)"', content)

quotes_db = {
    "en": load_quotes("bhagavad_gita_quotes.txt"),
    "hi": load_quotes("quotes_hi.txt"),
    "sa": load_quotes("quotes_sa.txt")
}

if not quotes_db["en"]:
    raise RuntimeError("No English quotes found")

@app.get("/")
async def root():
    return {
        "message": "gitaquotes API",
        "endpoint": "/api/v1/quotes/random"
    }

@app.get("/api/v1/quotes/random")
async def get_random_quote(lang: str = None):
    # Backward compatibility for existing integrations
    if not lang:
        return {"quote": random.choice(quotes_db["en"])}
    
    lang_key = lang.lower()
    
    if lang_key not in quotes_db or not quotes_db[lang_key]:
        return {
            "success": False,
            "message": "Language not supported or no quotes available. Supported: en, hi, sa"
        }
        
    lang_names = {"en": "English", "hi": "Hindi", "sa": "Sanskrit"}
    
    return {
        "success": True,
        "language": lang_names[lang_key],
        "quote": random.choice(quotes_db[lang_key])
    }

@app.get("/api/v1/quotes/{serial}")
async def get_quote_by_serial(serial: int, lang: str = "en"):
    lang_key = lang.lower()
    
    if lang_key not in quotes_db or not quotes_db[lang_key]:
        return {
            "success": False,
            "message": "Language not supported or no quotes available. Supported: en, hi, sa"
        }
        
    lang_names = {"en": "English", "hi": "Hindi", "sa": "Sanskrit"}
    quotes_list = quotes_db[lang_key]
    
    if serial < 1 or serial > len(quotes_list):
        return {
            "success": False,
            "message": f"Serial number out of bounds. Must be between 1 and {len(quotes_list)}"
        }
        
    return {
        "success": True,
        "language": lang_names[lang_key],
        "serial": serial,
        "quote": quotes_list[serial - 1]
    }

@app.get("/api/v1/languages")
async def get_languages():
    return {
        "success": True,
        "languages": ["English", "Hindi", "Sanskrit"],
        "supported_codes": ["en", "hi", "sa"]
    }
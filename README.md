# Bhagavad Gita Quotes API

A simple FastAPI API that returns a random Bhagavad Gita quote.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoint

### Get Random Quote

```http
GET /api/v1/quotes/random
```

### Response

```json
{
  "success": true,
  "data": {
    "quote": "You have the right to work, but never to the fruit of work."
  }
}
```

## API Docs

```text
http://localhost:8000/docs
```

## Tech Stack

- FastAPI
- Python
- Uvicorn

## License

MIT
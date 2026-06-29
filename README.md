# gitaquotes API

A simple FastAPI API that serves random Bhagavad Gita quotes for motivation, wisdom, and daily inspiration.

## Base URL

```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/
```

## Available Endpoints

### Get Random Bhagavad Gita Quote

```http
GET /api/v1/quotes/random
```

#### Example Request

```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/api/v1/quotes/random
```

#### Example Response

```json
{
  "success": true,
  "data": {
    "quote": "You have the right to work, but never to the fruit of work."
  }
}
```

## API Documentation

```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/docs
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Tech Stack

* FastAPI
* Python
* Uvicorn

## Future Updates

The API currently provides a single endpoint for random Bhagavad Gita quotes.

Planned additions:

* Quote by ID
* Daily Quote Endpoint
* Quote Categories
* Search Quotes
* Hindi Translations
* Verse References
* Rate Limiting
* API Versioning

## License

This project is licensed under the MIT License. See the LICENSE file for details.

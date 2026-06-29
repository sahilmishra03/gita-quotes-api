# gitaquotes API

A production-ready, free REST API delivering timeless wisdom and verified verses from the Bhagavad Gita for your applications. Features multi-language support (English, Hindi, Sanskrit) and requires no authentication.

## Base URL

```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/
```

## Available Endpoints

### 1. Get Random Quote

Fetches a randomly selected verse.

```http
GET /api/v1/quotes/random
```
**Query Parameters (Optional):**
- `lang`: Specify the language of the quote. Supported values: `en` (English), `hi` (Hindi), `sa` (Sanskrit).

#### Example Request
```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/api/v1/quotes/random?lang=hi
```

#### Example Response
```json
{
  "success": true,
  "language": "Hindi",
  "quote": "तुम्हारा अधिकार केवल कर्म करने में है..."
}
```

---

### 2. Get Quote by Serial (ID)

Fetches a specific verse using its serial number (1 to 101).

```http
GET /api/v1/quotes/{id}
```
**Path Parameters:**
- `id`: The serial number of the quote (1 - 101).

**Query Parameters (Optional):**
- `lang`: Specify the language (`en`, `hi`, `sa`). Defaults to `en`.

#### Example Request
```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/api/v1/quotes/5?lang=sa
```

#### Example Response
```json
{
  "success": true,
  "language": "Sanskrit",
  "serial": 5,
  "quote": "अहं मृत्युः सर्वाभिभूतः अद्यापि जायमानानां सर्वभूतानां प्रभवः।"
}
```

---

### 3. Get Available Languages

Returns a list of all currently supported languages and their codes.

```http
GET /api/v1/languages
```

#### Example Request
```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/api/v1/languages
```

#### Example Response
```json
{
  "success": true,
  "languages": [
    "English",
    "Hindi",
    "Sanskrit"
  ],
  "supported_codes": [
    "en",
    "hi",
    "sa"
  ]
}
```

## API Documentation

For the full interactive documentation, visit:
```text
https://geeta-quotes-api-d35f6cf2ee12.herokuapp.com/docs
```
*(Or view the beautifully styled custom documentation at `/website/docs.html`)*

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Then visit `http://127.0.0.1:8000` in your browser.

## Tech Stack

* **Backend**: FastAPI, Python, Uvicorn
* **Frontend UI**: HTML, Vanilla CSS (Glassmorphism), Vanilla JavaScript

## Future Updates

* Daily Quote Endpoint
* Quote Categories
* Search Quotes
* Verse References
* API Versioning

## License

This project is licensed under the MIT License. See the LICENSE file for details.

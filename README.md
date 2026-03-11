# Mini Data Query Simulation Engine

A lightweight backend service that simulates a Gen AI Analytics data query system, allowing non-technical teams to ask complex business questions and get instant insights.

## Live Demo
The API is now live at: https://mini-query-engine.onrender.com

You can test the API using the following curl commands:

```bash
# Process a query
curl -X POST "https://mini-query-engine.onrender.com/query" \
     -H "X-API-Key: secure_api_key_123" \
     -H "Content-Type: application/json" \
     -d '{"natural_language_query": "Find all products with sales above 1000"}'

# Get query explanation
curl "https://mini-query-engine.onrender.com/explain/1" \
     -H "X-API-Key: secure_api_key_123"

# Validate query
curl "https://mini-query-engine.onrender.com/validate/1" \
     -H "X-API-Key: secure_api_key_123"
```

## Features

- Natural language to SQL-like query translation
- Query explanation and validation
- Basic authentication
- SQLite database for query logging
- RESTful API endpoints

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yashwantharcot/mini-query-engine.git
cd mini-query-engine
```

2. Create and activate a virtual environment (optional but recommended):
# Mini Data Query Simulation Engine

Lightweight FastAPI backend and a small Streamlit UI that simulates a natural-language-to-SQL query pipeline. Use it to submit plain-language queries, store them in a local SQLite log, and get simple explanations and validation responses.

## Quick Start

Prerequisites: Python 3.11+ (3.10+ should work), pip installed.

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the backend API (from project root):

```bash
python -m uvicorn app.main:app --reload
```

The API listens on http://127.0.0.1:8000 by default.

3. (Optional) Start the Streamlit UI in a separate terminal:

```bash
streamlit run streamlit_app.py
```

Streamlit will open at http://localhost:8501 by default.

## Authentication

The API uses a simple header API key. The default key is defined in `app/routes.py`:

- Key value: `secure_api_key_123`
- Header: `X-API-Key` (the server also accepts `api-key` for compatibility)

You can change the key in [app/routes.py](app/routes.py#L1-L20).

## Endpoints

- POST /query — submit a natural-language query. JSON body:

```json
{ "natural_language_query": "Find all products with sales above 1000" }
```

Response example:

```json
{ "pseudo_sql_query": "SELECT * FROM data WHERE description LIKE '%Find all products with sales above 1000%';" }
```

- GET /explain/{query_id} — returns the saved explanation for a previously logged query.
- GET /validate/{query_id} — returns a basic validation message for the saved query.

All endpoints require the API key header.

## Database

This project uses SQLite. The database file `test.db` is created in the project root. Tables are created automatically when the app starts (the SQLAlchemy models live in `app/models.py`).

## Files of interest

- `app/main.py` — application entry point; starts FastAPI and creates DB tables.
- `app/routes.py` — API endpoints and authentication (change API key here).
- `app/models.py` — SQLAlchemy models (the `QueryLog` table).
- `app/database.py` — DB configuration (SQLite URL `sqlite:///./test.db`).
- `streamlit_app.py` — small Streamlit UI to interact with the API.

## Examples

Submit a query with curl:

```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: secure_api_key_123" \
  -d '{"natural_language_query":"Who are you?"}'
```

Get explanation for query id 1:

```bash
curl "http://127.0.0.1:8000/explain/1" -H "X-API-Key: secure_api_key_123"
```

## Troubleshooting

- 422 Unprocessable Entity on POST /query: make sure you send a JSON body with the `natural_language_query` field.
- `no such table: query_log`: ensure the app started successfully; `app/main.py` runs `Base.metadata.create_all(...)` on startup to create tables.
- Uvicorn launcher errors on Windows: run `python -m uvicorn app.main:app --reload` if `uvicorn` exe/launcher is misconfigured.

## Next steps

- Replace the simple pseudo-SQL generator with a real translator or an LLM backend.
- Add pagination and search for logged queries.
- Add tests and CI.

If you want, I can: update the API key storage to use environment variables, add more Streamlit controls, or add simple unit tests — tell me which and I'll implement it.


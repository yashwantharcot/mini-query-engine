# Mini Data Query Simulation Engine

A lightweight backend service that simulates a Gen AI Analytics data query system, allowing non-technical teams to ask complex business questions and get instant insights.

## Features

- Natural language to SQL-like query translation
- Query explanation and validation
- Basic authentication
- SQLite database for query logging
- RESTful API endpoints

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd mini-query-engine
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

### Authentication
All endpoints require an API key to be included in the request header:
```
X-API-Key: secure_api_key_123
```

### Endpoints

#### 1. Process Natural Language Query
```http
POST /query
Content-Type: application/json
X-API-Key: secure_api_key_123

{
    "natural_language_query": "Find all products with sales above 1000"
}
```

Response:
```json
{
    "pseudo_sql_query": "SELECT * FROM data WHERE description LIKE '%Find all products with sales above 1000%';"
}
```

#### 2. Get Query Explanation
```http
GET /explain/{query_id}
```

Response:
```json
{
    "explanation": "This query searches for records containing 'Find all products with sales above 1000' in the description field."
}
```

#### 3. Validate Query
```http
GET /validate/{query_id}
```

Response:
```json
{
    "validation": "Query is syntactically correct and ready for execution."
}
```

## Testing with curl

1. Process a query:
```bash
curl -X POST "http://localhost:8000/query" \
     -H "X-API-Key: secure_api_key_123" \
     -H "Content-Type: application/json" \
     -d '{"natural_language_query": "Find all products with sales above 1000"}'
```

2. Get query explanation:
```bash
curl "http://localhost:8000/explain/1" \
     -H "X-API-Key: secure_api_key_123"
```

3. Validate query:
```bash
curl "http://localhost:8000/validate/1" \
     -H "X-API-Key: secure_api_key_123"
```

## Project Structure

```
mini-query-engine/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── routes.py        # API endpoints
│   ├── models.py        # Database models
│   ├── database.py      # Database configuration
│   └── utils.py         # Utility functions
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Future Improvements

1. Implement more sophisticated natural language processing
2. Add support for different query types (aggregation, filtering, etc.)
3. Enhance error handling and validation
4. Add rate limiting and better security measures
5. Implement query caching
6. Add more comprehensive testing

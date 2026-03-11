# Mini Data Query Simulation Engine

Lightweight FastAPI backend + Streamlit UI that simulates a natural-language-to-SQL query pipeline. Submit plain-language queries, store them in a local SQLite log, and get simple explanations and validation responses.

## Live Backend (deployed)

- Backend API (Render): https://mini-query-engine-1.onrender.com

- Streamlit UI (deployed): https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app

## Quick Start (local)

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the backend API:

```bash
python -m uvicorn app.main:app --reload
```

3. In a separate terminal start the Streamlit UI (optional):

```bash
streamlit run streamlit_app.py
```

## Authentication

- Default API key (changeable in `app/routes.py` or via environment variable): `secure_api_key_123`
- Header: `X-API-Key` (also accepts `api-key` for compatibility)

## API Endpoints

- POST `/query` — submit a natural-language query
  - JSON body: `{ "natural_language_query": "Find all products with sales above 1000" }`
  - Response: `{ "pseudo_sql_query": "SELECT * FROM data WHERE description LIKE '%...%';" }`

- GET `/explain/{query_id}` — returns explanation for saved query
- GET `/validate/{query_id}` — basic validation message for saved query

Example (using deployed backend):

```bash
curl -X POST "https://mini-query-engine-1.onrender.com/query" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: secure_api_key_123" \
  -d '{"natural_language_query":"Who are you?"}'
```

## Deploying the Streamlit UI to Streamlit Community Cloud (no credit card)

1. Push your repository to GitHub (if not already):

```bash
git add .
git commit -m "prepare for deploy"
git push origin main
```

2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app** → select your repository, branch (`main`) and `streamlit_app.py` as the file to run.
4. In the Streamlit app settings set the following secrets (click **Settings → Secrets**):

- `API_URL` = `https://mini-query-engine-1.onrender.com`
- `API_KEY` = `secure_api_key_123`

5. Deploy — Streamlit will build and provide a public URL (e.g., `https://your-app-name.streamlit.app`).

Notes:
- The Streamlit app reads `API_URL` and `API_KEY` from environment variables; if you don't set them Streamlit will use `http://localhost:8000` and `secure_api_key_123` by default.
- If you prefer to host Streamlit on Render, create a second Web Service and use the start command:

```
streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
```

and set `API_URL` and `API_KEY` in Render's environment variables.

## What I can do next

- Deploy Streamlit for you (requires connecting your GitHub account to Streamlit Cloud). I can provide exact steps or a short checklist to follow.
- Add a short `deploy.md` with screenshots and the final public URLs.

If you want me to deploy the Streamlit app now, say "Deploy Streamlit" and confirm your GitHub repo name (or grant access). Otherwise, follow the Streamlit Cloud steps above and tell me the public URL so I can add it to the README and share instructions with users.

## Share with users

Provide the following URLs and instructions to users so they can try the app immediately:

- Streamlit UI (interactive): https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app
- Backend API (programmatic): https://mini-query-engine-1.onrender.com

Quick instructions for users:

1. Open the Streamlit UI URL in a browser and enter a natural language query, then click **Submit Query**.

2. Programmatic access (curl example):

```bash
curl -X POST "https://mini-query-engine-1.onrender.com/query" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: secure_api_key_123" \
  -d '{"natural_language_query":"Who are you?"}'
```

3. View saved query explanation:

```bash
curl "https://mini-query-engine-1.onrender.com/explain/1" -H "X-API-Key: secure_api_key_123"
```

Notes:
- The demo API key is `secure_api_key_123`. Replace or rotate the key for production use.
- The Render free instance may sleep after inactivity; allow ~30–60s for it to wake.

If you'd like, I can also open a small `deploy.md` with one-click links and usage snippets for sharing in your portfolio.

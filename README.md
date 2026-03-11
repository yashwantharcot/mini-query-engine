[![Streamlit Live](https://img.shields.io/badge/Streamlit-Online-brightgreen)](https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app) [![API (Render)](https://img.shields.io/badge/API-Render-blue)](https://mini-query-engine-1.onrender.com)

# Mini Data Query Simulation Engine

Live demo: https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app

About
- Small demo that translates plain-English queries into pseudo-SQL, logs them, and provides simple explanations. Built with FastAPI (backend), SQLite (store), and Streamlit (UI).

Try it
- Open the Streamlit demo (link above) and submit a query.
- Or call the API directly (curl):

```bash
curl -X POST "https://mini-query-engine-1.onrender.com/query" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: secure_api_key_123" \
  -d '{"natural_language_query":"Who are you?"}'
```

Notes
- Demo API key: `secure_api_key_123` (rotate for production).
- Render free instance may sleep after inactivity; expect a short cold start.

Tech
- FastAPI, Streamlit, SQLAlchemy, SQLite

Source
- https://github.com/yashwantharcot/mini-query-engine

For developer or deployment details see `deploy.md` in this repo.

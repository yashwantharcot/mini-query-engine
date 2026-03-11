# Deployment & Share Guide

This file contains screenshots, share-ready text, and quick instructions for sharing the deployed Mini Query Engine (FastAPI backend + Streamlit UI).

## Live URLs

- Streamlit UI: https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app
- Backend API: https://mini-query-engine-1.onrender.com

## Screenshots

(Place screenshot files in the repo or attach them to your portfolio page.)

1. Streamlit UI (live) — screenshot: `screenshot-streamlit-live.png`
2. Render service dashboard — screenshot: `screenshot-render-dashboard.png`
3. API docs page (/docs) — screenshot: `screenshot-api-docs.png`

Note: I have included example images while deploying. If you want these stored in the repo, add the PNG files to the project and reference them here.

## Share-ready text (short blurb) — copy/paste

Mini Data Query Simulation Engine — FastAPI backend + Streamlit UI demonstrating natural-language-to-SQL translation (pseudo-SQL) and query explanation. Try the live demo: https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app

## Social / portfolio snippets

- LinkedIn (short):

"Launched a small demo: Mini Data Query Simulation Engine — ask questions in plain English and see pseudo-SQL + explanations. Try it: https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app"

- GitHub README snippet (one-liner):

`Mini Data Query Simulation Engine — natural-language-to-SQL demo (FastAPI + Streamlit). Live demo: https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app`

## Embed link/button for portfolio

Use a simple anchor button linking to the Streamlit URL:

```html
<a href="https://mini-query-engine-eidxagwkwgaxfyeemnnqf6.streamlit.app" target="_blank" rel="noopener noreferrer">
  <button style="padding:8px 12px;border-radius:6px;background:#ff4b4b;color:white;border:none;">Open Mini Query Engine Demo</button>
</a>
```

## Quick copy/paste usage for users

1. Interactive (recommended): Open the Streamlit URL and enter a natural language query, then press **Submit Query**.

2. Programmatic (curl examples):

```bash
curl -X POST "https://mini-query-engine-1.onrender.com/query" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: secure_api_key_123" \
  -d '{"natural_language_query":"Who are you?"}'

curl "https://mini-query-engine-1.onrender.com/explain/1" -H "X-API-Key: secure_api_key_123"
```

## Security & tips

- The demo uses an API key `secure_api_key_123` by default (set in `app/routes.py` fallback). In production, rotate this key and set it only as an environment variable in Render and Streamlit Cloud.
- Render free instances may sleep after inactivity; expect a 20–60s cold start on first request.

## Want me to add this to your GitHub repo description?

Suggested repo description (one line):

"Mini Data Query Simulation Engine — Natural-language-to-SQL demo (FastAPI + Streamlit). Live demo available."

If you'd like, I can update the repo description text for you (I can commit the `deploy.md` now and push)."
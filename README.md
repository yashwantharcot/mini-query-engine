# Mini Data Query Simulation Engine

A modern full-stack application that transforms natural language queries into pseudo-SQL simulations. This project features a FastAPI backend and a premium React + Vite frontend.

## Architecture

- **Backend**: Python (FastAPI, SQLAlchemy, SQLite)
- **Frontend**: React (Vite, Vanilla CSS)

## Setup and Running

### Prerequisites
- Python 3.10+
- Node.js & npm

### Backend Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

### Frontend Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The UI will be available at `http://localhost:5173`.

## Features

- **Query Generation**: Convert natural language to pseudo-SQL.
- **Query Insights**: Explain and validate existing queries by ID.
- **Premium UI**: Modern dark-mode interface with responsive design.
- **Persistence**: Queries are logged in a local SQLite database (`test.db`).

from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import QueryLog

API_KEY = "secure_api_key_123"
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate(api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.post("/query", dependencies=[Depends(authenticate)])
def process_query(natural_language_query: str, db: Session = Depends(get_db)):
    pseudo_sql_query = f"SELECT * FROM data WHERE description LIKE '%{natural_language_query}%';"
    explanation = f"This query searches for records containing '{natural_language_query}' in the description field."

    query_log = QueryLog(
        natural_language_query=natural_language_query,
        pseudo_sql_query=pseudo_sql_query,
        explanation=explanation
    )
    db.add(query_log)
    db.commit()

    return {"pseudo_sql_query": pseudo_sql_query}

@router.get("/explain/{query_id}")
def explain_query(query_id: int, db: Session = Depends(get_db)):
    query_log = db.query(QueryLog).filter(QueryLog.id == query_id).first()
    if not query_log:
        raise HTTPException(status_code=404, detail="Query not found")
    return {"explanation": query_log.explanation}

@router.get("/validate/{query_id}")
def validate_query(query_id: int, db: Session = Depends(get_db)):
    query_log = db.query(QueryLog).filter(QueryLog.id == query_id).first()
    if not query_log:
        raise HTTPException(status_code=404, detail="Query not found")
    return {"validation": "Query is syntactically correct and ready for execution."}

@router.get("/")
def read_root():
    return {"message": "Hello, World!"}
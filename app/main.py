from fastapi import FastAPI
from .database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Delayed import to prevent circular import
from .routes import router
app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
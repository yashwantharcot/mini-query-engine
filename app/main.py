from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from .database import engine, Base
# Ensure models are imported before creating tables so SQLAlchemy registers them
from . import models


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Delayed import to prevent circular import
from .routes import router
app.include_router(router)

# Serve static files from the frontend build
frontend_dist = os.path.join(os.getcwd(), "frontend", "dist")
print(f"Checking for frontend at: {frontend_dist}")
if os.path.exists(frontend_dist):
    print("Frontend build found, mounting static files.")
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist, "assets")), name="static")

    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        file_path = os.path.join(frontend_dist, full_path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_dist, "index.html"))
else:
    print("Frontend build NOT found. Did the build script run?")

@app.get("/")
async def read_root():
    index_path = os.path.join(frontend_dist, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {
        "message": "Backend is running, but Frontend build was not found.",
        "path_checked": frontend_dist,
        "exists": os.path.exists(frontend_dist)
    }
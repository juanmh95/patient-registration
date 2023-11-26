
from fastapi import FastAPI

from app.api import patient
from app.config import get_settings
from app.database.database import init_db

settings = get_settings()
app = FastAPI()
app.include_router(patient.router, prefix="/api")

init_db()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
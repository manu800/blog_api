from fastapi import FastAPI
from database import engine, Base
from routers import posts
from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", version="1.0.0")

app.include_router(posts.router)


@app.get("/")
def root():
    return {"message": "Blog API is running", "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

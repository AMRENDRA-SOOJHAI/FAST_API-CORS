"""Main FastAPI application for Order Store API."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orders.router import order_router
# from database import Base, engine  # Uncommented to create tables if needed.

# Create database tables
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Store API", version="1.0.0")

@app.get("/")
async def home():
    """Root endpoint - Welcome message."""
    return {"msg": "Welcome To My Store"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Frontend UI port
    allow_credentials=True,
)

app.include_router(order_router)

# Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000

"""Main FastAPI application for Order Store API."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orders.router import order_router
import uvicorn
from logger import get_logger
import time
from fastapi import Request

# from database import Base, engine  # Uncommented to create tables if needed.
# Create database tables
# Base.metadata.create_all(bind=engine)

logger = get_logger(__name__)
app = FastAPI(title="Order Store API", version="1.0.0")

''' 
Define a global middleware for logging which logs each request method, URL path, response status code, and processing time.
'''
@app.middleware("http")
async def global_logger(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round(time.time() - start_time, 4)

    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Time: {process_time}s"
    )

    return response


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
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

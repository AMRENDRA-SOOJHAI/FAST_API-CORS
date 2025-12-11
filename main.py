from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orders.router import order_router

# # Create DB tables when create new DB:-
# Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def home():
    return {"msg": "Welcome To My Store"}

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500"],        # Orignal port where my UI is running .
    allow_credentials=True,
)
app.include_router(order_router)

from fastapi import FastAPI

app = FastAPI()
# -----------------------
# Home
# -----------------------

@app.get("/")
async def home():
    return {"msg": "Welcome To My Home"}

# -----------------------
# order router
# -----------------------

from fastapi.middleware.cors import CORSMiddleware

from orders.router import order_router
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],                            # allow all frontend .
    allow_origins = ["http://127.0.0.1:5500"],        # Orignal port where app UI is running through vs-code live server.
    # allow_origins = ["abc"],                        # If we try any another origin it will fail .

    allow_credentials=True,
)
app.include_router(order_router)


# -----------------------
# Product Related Routes
# -----------------------
@app.get("/products")
async def list_products():
    return [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Mobile", "price": 20000},
        {"id": 3, "name": "keyboard", "price": 2000},
        {"id": 4, "name": "mouse", "price": 1500},
    ]
# schemas.py
from pydantic import BaseModel

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    item: str
    quantity: int
    status: str = "Processing"

    # class Config:
    #     orm_mode = True  

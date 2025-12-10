
from fastapi import APIRouter

order_router = APIRouter()

created_order_list = []
order_id = 1

@order_router.post("/order/create")
async def create_order(customer_name:str, item: str, quantity: int):
    global order_id

    new_order = {
        "customer":customer_name,
        "order_id": order_id,
        "item": item,
        "quantity": quantity,
        "status": "Processing"
    }

    created_order_list.append(new_order)
    order_id += 1

    return {
        "msg": "Order Created",
        "order": new_order
    }


@order_router.get("/order/all")
async def get_all_orders():
    return created_order_list


@order_router.put("/order/update/order_id}")
async def update_order(order_id: int, status: str, item , quantity :int ):
    return {"msg": "Order Updated", "order_id": order_id,"item": item,"quantity": quantity ,"status": status}

@order_router.delete("/order/cancel/order_id")
async def cancel_order(order_id: int):
    return {"msg": "Order Cancelled", "order_id": order_id}
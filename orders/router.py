from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Tabels.order_tabel import Order_Tab

order_router = APIRouter(tags=["Orders"])


def order_to_dict(order: Order_Tab) -> dict:
    return {
        "id": order.id,
        "customer_name": order.customer_name,
        "item": order.item,
        "quantity": order.quantity,
        "status": order.status,
    }


# CREATE ORDER
@order_router.post("/order/create")
async def create_order(customer_name: str, item: str, quantity: int, db: Session = Depends(get_db)):

    new_order = Order_Tab(
        customer_name=customer_name,
        item=item,
        quantity=quantity,
        status="Processing",
    )

    db.add(new_order)
    db.commit()

    return {
        "msg": "Order Created",
        "order": order_to_dict(new_order)
    }



# GET ALL ORDERS
@order_router.get("/order/all")
async def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order_Tab).all()
    return [order_to_dict(i) for i in orders]


# UPDATE ORDER

@order_router.put("/order/update/{order_id}")
async def update_order(order_id: int,status: str, quantity: int, db: Session = Depends(get_db)):
    order = db.query(Order_Tab).filter(Order_Tab.id == order_id).first()
    if not order:
        return {"msg": "Order Not Found"}
    
    order.status = status
    order.quantity = quantity

    db.commit()

    return {
        "msg": "Order Updated", 
        "order": order_to_dict(order)
    }


# DELETE ORDER
@order_router.delete("/order/cancel/{order_id}")
async def cancel_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order_Tab).filter(Order_Tab.id == order_id).first()

    if not order:
        return {"msg": "Order Not Found"}

    db.delete(order)
    db.commit()

    return {
        "msg": "Order Cancelled", 
        "order_id": order_id
    }


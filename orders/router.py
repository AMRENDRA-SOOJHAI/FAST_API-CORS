"""Order management API router with CRUD operations."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Tabels.order_tabel import OrderTab
from Pydantic_response.order_response import OrderResponse

order_router = APIRouter(tags=["Orders"])


@order_router.post("/order/create", response_model=OrderResponse)
async def create_order(
    customer_name: str, item: str, quantity: int, db: Session = Depends(get_db)):
    """Create a new order with processing status."""
    new_order = OrderTab(
        customer_name=customer_name,
        item=item,
        quantity=quantity,
        status="Processing",
    )
    db.add(new_order)
    db.commit()
    return new_order


@order_router.get("/order/all", response_model=List[OrderResponse])
async def get_all_orders(db: Session = Depends(get_db)):
    """Retrieve all orders from database."""
    all_orders = db.query(OrderTab).all()
    return all_orders


@order_router.put("/order/update/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id: int, status: str, quantity: int, db: Session = Depends(get_db)):
    """Update order status and quantity by ID."""
    order_update = db.query(OrderTab).filter(OrderTab.id == order_id).first()
    if not order_update:
        raise HTTPException(status_code=404, detail="Order not found")
    order_update.status = status
    order_update.quantity = quantity
    db.commit()
    return order_update


@order_router.delete("/order/cancel/{order_id}")
async def cancel_order(order_id: int, db: Session = Depends(get_db)):
    """Delete/cancel order by ID."""
    delete_order = db.query(OrderTab).filter(OrderTab.id == order_id).first()
    if not delete_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(delete_order)
    db.commit()
    return {"msg": f"Order {order_id} cancelled successfully"}


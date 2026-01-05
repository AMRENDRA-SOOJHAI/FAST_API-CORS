from sqlalchemy import Column, Integer, String
from database import Base

class OrderTab(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String, default="Processing")


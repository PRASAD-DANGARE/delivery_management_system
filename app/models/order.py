from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.models.base import Base

class OrderStatus(PyEnum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    DELIVERED = "DELIVERED"
    DEFERRED = "DEFERRED"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    agent_id = Column(Integer, ForeignKey("agents.id"), nullable=True)

    warehouse = relationship("Warehouse", back_populates="orders")
    agent = relationship("Agent", back_populates="orders")
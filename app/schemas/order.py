from pydantic import BaseModel
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    DELIVERED = "DELIVERED"
    DEFERRED = "DEFERRED"

class OrderBase(BaseModel):
    customer_name: str
    address: str
    latitude: float
    longitude: float
    warehouse_id: int

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    status: OrderStatus
    agent_id: int | None = None
    class Config:
        orm_mode = True
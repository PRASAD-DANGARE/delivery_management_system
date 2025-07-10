from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    checked_in = Column(Boolean, default=False)
    total_km_today = Column(Float, default=0)
    total_time_today = Column(Float, default=0)

    warehouse = relationship("Warehouse", back_populates="agents")
    orders = relationship("Order", back_populates="agent")
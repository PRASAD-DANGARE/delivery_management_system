from fastapi import FastAPI
from app.routers import order
from app.models import base, agent, order as order_model, warehouse
from app.database import engine

# Create tables
base.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(order.router, prefix="/orders", tags=["Orders"])
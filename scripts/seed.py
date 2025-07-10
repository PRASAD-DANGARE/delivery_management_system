import random
from faker import Faker
from app.database import SessionLocal, engine
from app.models.agent import Agent
from app.models.order import Order, OrderStatus
from app.models.warehouse import Warehouse
from app.models.base import Base

# Create tables if not already present
Base.metadata.create_all(bind=engine)

fake = Faker()
db = SessionLocal()

def seed_warehouses(n=10):
    for _ in range(n):
        warehouse = Warehouse(
            name=fake.company(),
            latitude=fake.latitude(),
            longitude=fake.longitude()
        )
        db.add(warehouse)
    db.commit()

def seed_agents_per_warehouse(count=20):
    warehouses = db.query(Warehouse).all()
    for wh in warehouses:
        for _ in range(count):
            agent = Agent(
                name=fake.name(),
                warehouse_id=wh.id,
                checked_in=True
            )
            db.add(agent)
    db.commit()

def seed_orders_per_agent(count=60):
    agents = db.query(Agent).all()
    for agent in agents:
        for _ in range(count):
            order = Order(
                customer_name=fake.name(),
                address=fake.address(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                warehouse_id=agent.warehouse_id,
                status=OrderStatus.PENDING
            )
            db.add(order)
    db.commit()

if __name__ == "__main__":
    seed_warehouses()
    seed_agents_per_warehouse()
    seed_orders_per_agent()
    print("✅ Database seeded successfully")
# test_allocation.py

from app.database import SessionLocal
from app.models.order import Order, OrderStatus
from app.services.allocation import allocate_orders

# Run allocation
print("🚚 Running allocation...")
allocate_orders()

# Create a DB session to inspect results
db = SessionLocal()

# Summary
assigned = db.query(Order).filter(Order.status == OrderStatus.ASSIGNED).count()
deferred = db.query(Order).filter(Order.status == OrderStatus.DEFERRED).count()
pending = db.query(Order).filter(Order.status == OrderStatus.PENDING).count()

print(f"✅ Assigned Orders: {assigned}")
print(f"⏸️ Deferred Orders: {deferred}")
print(f"📦 Pending Orders: {pending}")

# List some assigned orders
print("\n📋 Sample assigned orders:")
for order in db.query(Order).filter(Order.status == OrderStatus.ASSIGNED).limit(5).all():
    print(f"Order ID: {order.id}, Agent ID: {order.agent_id}, Status: {order.status}")

db.close()
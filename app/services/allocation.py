from app.models.agent import Agent
from app.models.order import Order, OrderStatus
from utils.distance import haversine_distance
from app.database import SessionLocal

MAX_KM = 100
MAX_TIME_MIN = 600  # 10 hours
KM_TO_MIN = 5

def allocate_orders():
    db = SessionLocal()
    try:
        agents = db.query(Agent).filter(Agent.checked_in == True).all()
        orders = db.query(Order).filter(Order.status == OrderStatus.PENDING).all()

        for agent in agents:
            warehouse = agent.warehouse
            remaining_km = MAX_KM
            remaining_time = MAX_TIME_MIN

            assigned = 0
            for order in orders:
                if order.warehouse_id != agent.warehouse_id or order.status != OrderStatus.PENDING:
                    continue

                distance = haversine_distance(
                    (warehouse.latitude, warehouse.longitude),
                    (order.latitude, order.longitude)
                )
                time_needed = distance * KM_TO_MIN

                if distance <= remaining_km and time_needed <= remaining_time:
                    order.agent_id = agent.id
                    order.status = OrderStatus.ASSIGNED
                    db.add(order)

                    remaining_km -= distance
                    remaining_time -= time_needed
                    assigned += 1

            print(f"Agent {agent.id} assigned {assigned} orders.")
        db.commit()
    finally:
        db.close()
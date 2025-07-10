from app.services.allocation import allocate_orders
from datetime import datetime

def daily_allocation_job():
    print(f"[{datetime.now()}] Running daily order allocation...")
    allocate_orders()

if __name__ == "__main__":
    daily_allocation_job()
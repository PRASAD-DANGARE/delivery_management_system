# 🛵 Delivery Management System

A FastAPI-based system to assign delivery orders to agents while optimizing time, distance, and cost.

---

## 🚀 Objective

Efficiently assign delivery **orders** to **agents** each morning based on constraints like time, distance, and profitability.

---

## 🧱 Features

- ✅ Auto-assign orders to agents at check-in based on 10hr/100km limits
- ✅ Haversine distance calculation for geo-routing
- ✅ Order deferral logic for unassignable deliveries
- ✅ Agent earnings tier logic (₹35/order for 25+, ₹42/order for 50+)
- ✅ Daily summary of assignments
- ✅ Swagger support for API testing

---

## ⚙️ Tech Stack

| Layer         | Tech                      |
|---------------|---------------------------|
| Language      | Python                    |
| Framework     | FastAPI                   |
| Database      | SQLite (default) / PostgreSQL / MySQL |
| ORM           | SQLAlchemy                |
| Background Job| Manual / Celery / APScheduler-ready |
| API Docs      | Swagger UI (`/docs`)      |

---

## 🏁 Setup Instructions

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🔄 Background Job (via Celery)

```bash
celery -A app.background_tasks.worker worker --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

---

## ⚙️ Allocation Logic

Run manually:

```bash
$env:PYTHONPATH = "."
python app/background_tasks/allocation.py
```

### Constraints

- Max 10 hours (600 minutes) per agent
- Max 100 km travel/day
- 1 km = 5 minutes travel time

### Profitability

| Orders Delivered | Rate (per order) |
|------------------|------------------|
| < 25             | ₹20 (default)    |
| 25+              | ₹35              |
| 50+              | ₹42              |

---

## 🧪 How to Test

### ✅ Via Swagger

- Start app with `uvicorn main:app --reload`
- Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Use `/orders/` POST to create order
- Use `/orders/` GET to list orders
- Add `/orders/summary` for allocation stats (optional)

### ✅ Via Python script

Create `test_allocation.py`:

```python
from app.services.allocation import allocate_orders
from app.database import SessionLocal
from app.models.order import Order, OrderStatus

allocate_orders()

db = SessionLocal()
print("Assigned:", db.query(Order).filter(Order.status == OrderStatus.ASSIGNED).count())
print("Pending:", db.query(Order).filter(Order.status == OrderStatus.PENDING).count())
print("Deferred:", db.query(Order).filter(Order.status == OrderStatus.DEFERRED).count())
db.close()
```

---

## 📁 Folder Structure

```
delivery_management_system/
│
├── app/
│   ├── models/        # SQLAlchemy models
│   ├── routers/       # FastAPI endpoints
│   ├── services/      # Allocation logic
│   ├── schemas/       # Pydantic models
│   ├── background_tasks/  # Job scripts & Celery workers
│   └── utils/         # Distance calculations
│
├── scripts/           # Data seeding
├── test_allocation.py # Test file
├── main.py            # FastAPI app entry
└── requirements.txt
```

---

## 📌 TODO / Bonus Ideas

- ⏰ Automate allocation with APScheduler/Celery
- 📊 Add `/metrics` route for cost/agent stats
- 🧪 Add `pytest` test coverage
- 📤 Export results to CSV or JSON

---

## 👨‍💻 Author

Made with ❤️ for backend system design evaluations.
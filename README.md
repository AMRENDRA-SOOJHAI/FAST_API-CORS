# 🚀 FAST_API-CORS – Order Store API

A simple **FastAPI-based Order Store application** demonstrating **CORS handling**, **SQLite database integration**, and a **basic frontend dashboard** using plain HTML, CSS, and JavaScript.

This project is ideal for beginners who want to understand:

* FastAPI project structure
* CORS configuration
* SQLAlchemy with SQLite
* API ↔ Frontend communication

---

## 📌 Features

* ✅ FastAPI backend with clean structure
* ✅ SQLite database (`Orders.db`)
* ✅ SQLAlchemy ORM
* ✅ Pydantic response models
* ✅ CORS enabled for frontend access
* ✅ Simple frontend dashboard (HTML + JS)
* ✅ Fetch & display orders in UI

---

## 🗂️ Project Structure

```
FAST_API/
│
├── orders/
│   ├── __init__.py
│   ├── router.py          # API routes for orders

|   Tabels/
|   |-- order_tabel.py
│
├── Pydantic_response/
│   └── order_response.py  # Pydantic response schema
│
├── database.py            # Database configuration
├── main.py                # FastAPI app entry point
├── Orders.db              # SQLite database
├── front_end.html         # Simple frontend UI
├── pyproject.toml
├── poetry.lock
```

---

## ⚙️ Tech Stack

* **Backend**: FastAPI
* **Database**: SQLite + SQLAlchemy
* **Validation**: Pydantic
* **Frontend**: HTML, CSS, JavaScript
* **Server**: Uvicorn

---

## 🧠 How CORS Is Used

CORS is enabled so that the frontend running on a different port can access the FastAPI backend.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
)
```

This allows requests from the frontend UI served via Live Server or similar tools.

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment (optional)

```bash
python -m venv env
source env/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

*(If using Poetry, run `poetry install`)*

---

### 3️⃣ Run FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### 4️⃣ Run Frontend UI

Open `front_end.html` using **Live Server** or directly in browser.

Frontend will call:

```
GET http://127.0.0.1:8000/order/all
```

---

## 📦 API Endpoints (Example)

| Method | Endpoint     | Description      |
| ------ | ------------ | ---------------- |
| GET    | `/`          | Health check     |
| GET    | `/order/all` | Fetch all orders |

---

## 🗄️ Database

* SQLite database file: `Orders.db`
* SQLAlchemy session handled via dependency injection

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 📸 UI Preview

The frontend dashboard displays:

* Total order count
* Order cards with details
* Loader while fetching data

---

## 🎯 Learning Purpose

This repository is created for:

* Practicing FastAPI basics
* Understanding CORS issues
* Learning backend ↔ frontend integration
* API response modeling with Pydantic

---

## 🙌 Author

**Amrendra Singh**
📍 India
💼 Data & Backend Enthusiast

---

## ⭐ If you like this repo

Give it a ⭐ and feel free to fork or raise issues!

Happy Coding 🚀

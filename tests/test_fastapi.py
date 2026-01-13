from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from database import get_db

client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome To My Store"}


# # -------------------------------
# # Fake DB session
# def override_get_db():
#     db = MagicMock(spec=Session)
#     yield db
# app.dependency_overrides[get_db] = override_get_db


# # -------------------------------
# # TEST: create order
# def test_create_order():
#     response = client.post(
#         "/order/create",
#         params={
#             "customer_name": "Alankar",
#             "item": "Laptop",
#             "quantity": 2,
#         },
#     )

#     assert response.status_code == 200
#     assert response.json()["customer_name"] == "Alankar"
#     assert response.json()["item"] == "Laptop"
#     assert response.json()["quantity"] == 2
#     assert response.json()["status"] == "Processing"

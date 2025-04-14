import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login_and_portfolio_flow():
    """
    Test the end-to-end flow of user registration, login, and portfolio management.
    Verify user registration and login functionality, including token generation.
    Test adding and retrieving portfolio entries for the authenticated user.
    """
    user = {"email": "demo@example.com", "password": "demo123"}
    
    res = client.post("/auth/register", json=user)
    assert res.status_code == 200 or res.status_code == 400
    
    res = client.post("/auth/login", json=user)
    assert res.status_code == 200
    token = res.json()["access_token"]

    headers = {'Content-Type': 'application/json'}
    fund = {"fund_name": "Demo Fund", "current_value": 10000.0}
    
    res = client.post(f"/portfolio/?token={token}", json=fund, headers=headers)
    assert res.status_code == 200
    assert res.json()["fund_name"] == fund["fund_name"]

    res = client.get(f"/portfolio/?token={token}", headers=headers)
    assert res.status_code == 200
    assert len(res.json()) >= 1

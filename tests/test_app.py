import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["dang_ol"] == "pong"
    assert data["status"] == "ok"

def test_check_valid_host():
    response = client.get("/check/google.com")
    assert response.status_code == 200
    data = response.json()
    assert data["host"] == "google.com"
    assert data["status"] == "ok"
    assert "result" in data

def test_check_invalid_host():
    host = "invalid-domain"
    response = client.get(f"/check/{host}")
    assert response.status_code == 200
    data = response.json()
    assert data["host"] == host
    assert data["status"] == "ok"
    assert "result" in data
    assert data["result"] == {}
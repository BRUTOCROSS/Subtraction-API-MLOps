from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Subtraction API is running"
    }

def test_subtraction():
    response = client.get("/subtract?num1=20&num2=10")
    assert response.status_code == 200
    assert response.json()["result"] == 10

def test_negative_result():
    response = client.get("/subtract?num1=10&num2=20")
    assert response.status_code == 200
    assert response.json()["result"] == -10

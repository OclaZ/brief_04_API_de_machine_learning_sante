import pytest 
from app.main import app
from fastapi.testclient import TestClient
def test_predict():
    client = TestClient(app)
    response = client.post("/predict", json={
        "age": 55,
        "gender": 1,
        "pressurehight": 140,
        "pressurelow": 90,
        "glucose": 110,
        "kcm": 5.5,
        "troponin": 0.03,
        "impulse": 80
        })
    assert response.status_code == 200
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

VALID_PAYLOAD = {
    "age": 52,
    "sex": "M",
    "chest_pain_type": "ATA",
    "resting_bp": 125,
    "cholesterol": 212,
    "fasting_bs": 0,
    "resting_ecg": "Normal",
    "max_hr": 168,
    "exercise_angina": "N",
    "oldpeak": 1.0,
    "st_slope": "Up",
}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_valid_payload():
    response = client.post("/predict", json=VALID_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    assert "prediction" in body
    assert 0.0 <= body["probability"] <= 1.0

def test_predict_invalid_enum_rejected():
    bad_payload = {**VALID_PAYLOAD, "sex": "X"}
    response = client.post("/predict", json=bad_payload)
    assert response.status_code == 422

def test_predict_invalid_field_rejected():
    bad_payload = {"oops": "daisy"}
    response = client.post("/predict", json=bad_payload)
    assert response.status_code == 422
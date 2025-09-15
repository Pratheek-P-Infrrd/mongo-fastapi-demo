import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_validate_document_success():
    payload = {
        "document_type": "paystub",
        "borrower_name": "John Doe",
        "employer_name": "ABC Corp",
        "pay_period_start": "2024-01-01",
        "pay_period_end": "2024-01-15",
        "gross_income": 5000.00
    }

    response = client.post("/api/v1/documents/validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "valid"
    assert "document_id" in data
    assert data["validation_errors"] == []

def test_validate_document_failure():
    payload = {
        "document_type": "paystub",
        "borrower_name": "",
        "employer_name": "ABC Corp",
        "pay_period_start": "2024-01-20",
        "pay_period_end": "2024-01-15",
        "gross_income": -5000
    }

    response = client.post("/api/v1/documents/validate", json=payload)
    # FastAPI + Pydantic returns 422 for validation errors
    assert response.status_code == 422

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, débutant !"}

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_unknown_item():
    response = client.delete("/items/99999")
    assert response.status_code == 404

def test_get_unknown_item():
    response = client.get("/items/99999")
    assert response.status_code == 404
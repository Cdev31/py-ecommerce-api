from fastapi.testclient import TestClient
from server import app

client = TestClient( app )

def test_prob():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "Greeting": "Hello" }
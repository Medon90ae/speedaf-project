
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_hello():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"msg": "Hello Speedaf"}

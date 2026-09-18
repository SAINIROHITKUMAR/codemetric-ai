from app import create_app

def test_health():
    client = create_app().test_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json["status"] == "success"

def test_analyze():
    client = create_app().test_client()
    response = client.post("/api/analyze", json={"code": "def add(a,b):\n    return a+b"})
    assert response.status_code == 200
    assert "quality_score" in response.json["data"]

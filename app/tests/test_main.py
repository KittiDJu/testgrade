from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_grade():
    response = client.get("/grade/85")
    assert response.status_code == 200
    assert response.json() == {"grade": "A"}

    response = client.get("/grade/75")
    assert response.status_code == 200
    assert response.json() == {"grade": "B"}

    response = client.get("/grade/65")
    assert response.status_code == 200
    assert response.json() == {"grade": "C"}

    response = client.get("/grade/55")
    assert response.status_code == 200
    assert response.json() == {"grade": "D"}

    response = client.get("/grade/45")
    assert response.status_code == 200
    assert response.json() == {"grade": "F"}

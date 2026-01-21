from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_endpoint():
    response = client.post(
        "/generate",
        params={"prompt": "a red apple on a table"}
    )

    assert response.status_code == 200
    data = response.json()

    assert "image_path" in data
    assert "image_base64" in data
    assert "clip_analysis" in data
    assert "segmentation" in data

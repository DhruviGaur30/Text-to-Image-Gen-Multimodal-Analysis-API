from fastapi.testclient import TestClient
from app.main import app
from PIL import Image
import io

client = TestClient(app)

def test_analyze_endpoint():
    # create a dummy image
    image = Image.new("RGB", (128, 128), color="red")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    response = client.post(
        "/analyze",
        files={"file": ("test.png", buffer, "image/png")}
    )

    assert response.status_code == 200
    data = response.json()

    assert "image_path" in data
    assert "clip_analysis" in data
    assert "segmentation" in data

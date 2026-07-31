from fastapi.testclient import TestClient
from validators.api import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.parametrize(
        "email,expected",
        [
            ("test@gmail.com", True),
            ("test123@gmail.com", True),
            ("123test@gmail.com", True),
            ("Test@gmail.com", True),
            ("T.est@gmail.com", True),
            ("T-est@gmail.com", True),
            ("-+Test%@gmail.com", True),
            ("Test@g.mail.c", True),
            ("Test@gmail.com", True),
            ("Test@gmai123l.com", True),
            ("Test@gmail-.com", True),

            ("testgmail.com", False),
            ("test@gmail.c", False),
            ("test@gmail..com", False),
            ("test@gmail.com.", False),
            (".test@gmail.com", False),
            ("test.@gmail.com", False),
            ("test@.gmail.com", False),
            ("test@-gmail.com", False),
            ("test@gmail.com.", False),
            ("test@gmail.com-", False),
            ("test@-gmail.com", False),
            ("тест@gmail.com", False),
            ("test@gm%ail.com", False)
        ]
)
async def test_check_email_endpoint(client, email:str, expected:bool):
    response = client.post("/check/email/", json={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert "is_valid" in data, "Response missing 'is_valid' field"
    assert "message" in data, "Response missing 'message' field"
    assert data["is_valid"] == expected
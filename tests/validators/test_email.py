import pytest
from validators.email import CheckEmail
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
async def test_check_email(email:str, expected:bool):
    req = CheckEmail.Request(email=email)
    assert (await CheckEmail.check_email(req=req)).is_valid == expected
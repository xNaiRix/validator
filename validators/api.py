from fastapi import FastAPI
from validators.email import CheckEmail
from dotenv import load_dotenv
import os
app = FastAPI()


@app.post("/check/email/", response_model = CheckEmail.Response)
async def check_email(req:CheckEmail.Request):
    load_dotenv()
    PORT = os.getenv("PORT", "1000")
    assert PORT == 1000
    logs = await CheckEmail.check_email(req)
    print(logs)
    return logs

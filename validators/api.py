from fastapi import FastAPI
from validators.email import CheckEmail
app = FastAPI()

@app.post("/check/email/", response_model = CheckEmail.Response)
async def check_email(req:CheckEmail.Request):
    logs = await CheckEmail.check_email(req)
    print(logs)
    return logs

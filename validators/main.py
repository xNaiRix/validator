from validators.api import app
import uvicorn
from dotenv import load_dotenv
import os
load_dotenv()
if __name__=="__main__":
    BACKEND_IP = os.getenv("BACKEND_API", "localhost")
    PORT = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "main:app",
        host = BACKEND_IP,
        port = PORT,
        reload=True
    )#
    
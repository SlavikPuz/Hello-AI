from fastapi import FastAPI
from predictor import generate_message
from models import MessageResponse

app = FastAPI()


@app.get("/", response_model=MessageResponse)
def hello():
    return MessageResponse(message=generate_message("AI"))
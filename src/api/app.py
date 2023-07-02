import uvicorn
from fastapi import FastAPI
from models import *
import sqlalchemy

class ToDoAPI:
    def initialize(self):
        @self.app.get("/")
        def home():
            return {"Test": "Is Alive"}

        @self.app.get("/calendar/month={month}")
        def test(month:int):
            return month
    
    def start(self, port=8000, host="0.0.0.0"):
        uvicorn.run(self.app, port=port, host=host)

    def __init__(self) -> None:
        self.app = FastAPI()

        self.initialize()
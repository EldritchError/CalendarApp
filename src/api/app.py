import uvicorn
from fastapi import FastAPI

class CalendarAPI:
    def initialize(self):
        @self.app.get("/")
        def home():
            return {"Test": "Is Alive"}
    
    def start(self, port=8000, host="0.0.0.0"):
        uvicorn.run(self.app, port=port, host=host)

    def __init__(self) -> None:
        self.app = FastAPI()

        self.initialize()
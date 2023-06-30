import uvicorn
from fastapi import FastAPI

class CalendarAPI:
    def initialize(self):
        @self.app.get("/")
        def home():
            return {"Test": "Is Alive"}
        
        @self.app.get("/calendar/{month}")
        def calendar_month(int month):
            # get data from database
            data = {1: {("13:00", "14:00"): "Meeting"}}
            return data
    
    def start(self, port=8000, host="0.0.0.0"):
        uvicorn.run(self.app, port=port, host=host)

    def __init__(self) -> None:
        self.app = FastAPI()

        self.initialize()
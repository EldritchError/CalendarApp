import uvicorn
from fastapi import FastAPI
from models import *

class CalendarAPI:
    def initialize(self):
        @self.app.get("/")
        def home():
            return {"Test": "Is Alive"}

        @self.app.get("/calendar/month={month}")
        def test(month:int):
            day = 1
            my_card = ScheduledToDoCard(id=1, due_date=1, pattern=CalendarPattern(days_of_the_week=DaysOfTheWeek(False, True, False, True, False, True)))
            return {day: {"start_time": "13:00", "end_time": "14:00", "cards": ScheduledToDoCard}}
    
    def start(self, port=8000, host="0.0.0.0"):
        uvicorn.run(self.app, port=port, host=host)

    def __init__(self) -> None:
        self.app = FastAPI()

        self.initialize()
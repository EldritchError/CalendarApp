import time
import datetime

class CalendarPattern:
    def __init__(self, days_of_the_week={'MONDAY': False, 'TUESDAY': False, 'WEDNESDAY': False, 'THURSDAY': False, 'FRIDAY': False, 'SATURDAY': False, 'SUNDAY': False}, 
                 week_interval=1, month_interval=1, year_interval=1) -> None:
        self.days_of_the_week = days_of_the_week
        self.week_interval = week_interval
        self.month_interval = month_interval
        self.year_interval = year_interval

class Card:
    def __init__(self, id, name="", text="") -> None:
        self.id = id
        self.name = name
        self.text = text

class ToDoCard(Card):
    def __init__(self, id, name="", text="", done=False) -> None:
        super().__init__(id, name, text)
        self.done = done

class ScheduledToDoCard(ToDoCard):
    def __init__(self, id, due_date, pattern:CalendarPattern, name="", text="", done=False) -> None:
        super().__init__(id, name, text, done)
        self.due_date = due_date
        self.pattern = pattern
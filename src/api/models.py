import datetime
import uuid

class Card:
    def __init__(self, name="", text="") -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.text = text

class ToDoCard(Card):
    def __init__(self, name="", text="", done=False) -> None:
        super().__init__(name, text)
        self.done = done

class SchedulePattern:
    def __init__(self, monday=False, tuesday=False, wednesday=False, 
                 thursday=False, friday=False, saturday=False, sunday=False, 
                 repeating_every_x_week=1, repeating_every_x_month=1, repeating_every_x_year=1) -> None:
        self.days_of_week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
        self.repeating_every_x_week = repeating_every_x_week
        self.repeating_every_x_month = repeating_every_x_month
        self.repeating_every_x_year = repeating_every_x_year

class ScheduledToDoCard(ToDoCard):
    def __init__(self, date:datetime.date, start_time=None, end_time=None, name="", text="", done=False, repeating=False) -> None:
        super().__init__(name, text, done)
        self.date = date
        self.scheduled_with_time_of_day = start_time != None or end_time != None
        if start_time != None:
            self.start_time = start_time
        else:
            self.start_time = datetime.time(0, 0)
        if end_time != None:
            self.end_time = end_time
        else:
            self.end_time = datetime.time(23, 59, 59)
        self.repeating = repeating
        self.pattern = SchedulePattern()
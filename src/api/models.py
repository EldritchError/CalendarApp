import time
import datetime

class Card:
    def __init__(self, id, name="", text="") -> None:
        self.id = id
        self.name = name
        self.text = text

class ToDoCard(Card):
    def __init__(self, id, name="", text="", done=False) -> None:
        super().__init__(id, name, text)
        self.done = done

def time_string_to_int(time_str:str):
    hour, minute = time_str.split(":")
    result = int(hour) * 60 + int(minute)
    return result

class EndTimeWithoutStartTimeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Day:
    def add_card(self, card:Card, start_time:str, end_time:str):
        if start_time == None and end_time == None:
            self.cards.append(card)
        elif start_time != None:
            if end_time == None:
                self.scheduled_cards[start_time + "--" + start_time] = card
            else:
                self.scheduled_cards[start_time + "--" + end_time] = card
        else:
            raise EndTimeWithoutStartTimeException()

    def __init__(self) -> None:
        self.cards = []
        # Key definition: start time -> "hour:minute--hour:minute" <- end time
        self.scheduled_cards = {}

class Week:
    def __init__(self, monday=Day(), tuesday=Day(), wednesday=Day(), thursday=Day(), friday=Day(), saturday=Day(), sunday=Day()) -> None:
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
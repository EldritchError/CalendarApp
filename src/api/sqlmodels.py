from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import uuid
import datetime

class Base(DeclarativeBase):
    pass


class Card(Base):
    __tablename__ = "card"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)       
    name: Mapped[str] = mapped_column(String(255))
    text: Mapped[Optional[str]]
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class ToDoCard(Base):
    __tablename__ = "to_do_card"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)       
    name: Mapped[str] = mapped_column(String(255))
    text: Mapped[Optional[str]]
    done: Mapped[bool] = mapped_column(bool)
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class SchedulePattern:
    def __init__(self, monday=False, tuesday=False, wednesday=False, 
                 thursday=False, friday=False, saturday=False, sunday=False, 
                 repeating_every_x_week=1, repeating_every_x_month=1, repeating_every_x_year=1) -> None:
        self.days_of_week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
        self.repeating_every_x_week = repeating_every_x_week
        self.repeating_every_x_month = repeating_every_x_month
        self.repeating_every_x_year = repeating_every_x_year

class ScheduledToDoCard(ToDoCard):
    __tablename__ = "scheduled_to_do_card"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)       
    name: Mapped[str] = mapped_column(String(255))
    text: Mapped[Optional[str]]
    done: Mapped[bool] = mapped_column(bool)
    date: Mapped[datetime.date] = mapped_column(datetime.date)
    start_time: Mapped[datetime.time] = mapped_column(datetime.time)
    end_time: Mapped[datetime.time] = mapped_column(datetime.time)
    repeating: Mapped[bool] = mapped_column(bool)
    pattern: Mapped[uuid.UUID] = mapped_column(bool) # ToDo: implement as foreign key
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
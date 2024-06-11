"""
This module contains the constants used in the application.
"""
import pytest
from datetime import datetime
from src.journey import Journey
from src.utils import InvalidTimeFormat


def test_journey_creation():
    journey = Journey("A", "B")
    assert journey.start_station == "A"
    assert journey.end_station == "B"
    assert journey.timetable == {}


def test_set_timetable():
    journey = Journey("A", "B")
    time_table = {
        "departure_time": ["08:00", "12:00", "16:00"],
        "duration": "01:00"
    }
    journey.timetable = time_table
    assert journey.timetable == time_table


def test_invalid_time_format():
    journey = Journey("A", "B")
    time_table = {
        "departure_time": ["08:00", "12:00", "invalid"],
        "duration": "01:00"
    }
    with pytest.raises(InvalidTimeFormat):
        journey.timetable = time_table


def test_arrival_time():
    journey = Journey("A", "B")
    time_table = {
        "departure_time": ["08:00"],
        "duration": "01:00"
    }
    journey.timetable = time_table
    assert journey.arrival_time("08:00") == datetime.strptime("09:00", "%H:%M")


def test_departure_arrival_time_table():
    journey = Journey("A", "B")
    time_table = {
        "departure_time": ["08:00", "12:00"],
        "duration": "01:00"
    }
    journey.timetable = time_table
    assert journey.departure_arrival_time_table() == [("08:00", "09:00"), ("12:00", "13:00")]

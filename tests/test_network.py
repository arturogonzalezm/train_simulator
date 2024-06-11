"""
This module contains the test cases for the network module.
"""

import pytest

from src.exceptions import InvalidStation
from src.journey import Journey
from src.network import TrainNetwork


def create_sample_journeys():
    journey1 = Journey("A", "B")
    journey1.timetable = {
        "departure_time": ["08:00", "12:00", "16:00"],
        "duration": "01:00"
    }
    journey2 = Journey("B", "C")
    journey2.timetable = {
        "departure_time": ["09:00", "13:00", "17:00"],
        "duration": "01:00"
    }
    journey3 = Journey("C", "D")
    journey3.timetable = {
        "departure_time": ["10:00", "14:00", "18:00"],
        "duration": "01:00"
    }
    journey4 = Journey("B", "D")
    journey4.timetable = {
        "departure_time": ["10:00", "14:00", "18:00"],
        "duration": "02:00"
    }
    return [journey1, journey2, journey3, journey4]


def test_network_creation():
    train_network = TrainNetwork()
    assert train_network.journey == {}
    assert train_network.all_station == set()


def test_build_network_from_journeys():
    train_network = TrainNetwork()
    journeys = create_sample_journeys()
    train_network.build_network_from_journey(journeys)
    assert "A" in train_network.all_station
    assert "D" in train_network.all_station
    assert len(train_network.journey["A"]) == 1
    assert len(train_network.journey["B"]) == 2


def test_invalid_station():
    train_network = TrainNetwork()
    journeys = create_sample_journeys()
    train_network.build_network_from_journey(journeys)
    with pytest.raises(InvalidStation):
        train_network.find_route("A", "Z")

"""
This module contains the test cases for the strategies module.
"""

from collections import defaultdict

from src.journey import Journey
from src.network import TrainNetwork


class MockTrainNetwork(TrainNetwork):
    """
    Mock TrainNetwork class for testing
    """
    def __init__(self):
        """
        Initialize the MockTrainNetwork.
        """
        super().__init__()
        # Ensure the network has all necessary stations and journeys
        self.all_station = {"A", "B", "E"}
        self.journey = defaultdict(list)

        journey1 = Journey("A", "B")
        journey1.timetable = {
            "departure_time": ["08:00", "12:00", "16:00"],
            "duration": "01:00"
        }
        self.journey["A"].append(journey1)

        journey2 = Journey("B", "E")
        journey2.timetable = {
            "departure_time": ["09:00", "13:00", "17:00"],
            "duration": "02:00"
        }
        self.journey["B"].append(journey2)




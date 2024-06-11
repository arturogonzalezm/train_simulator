"""
This module contains the constants used in the application.
"""
import heapq
from collections import defaultdict
from datetime import timedelta

from .exceptions import InvalidStation
from .utils import convert_to_timedelta


class TrainNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TrainNetwork, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.journey = defaultdict(list)
            self.all_station = set()
            self.initialized = True

    def _journey_instance(self, start_station):
        if start_station not in self.journey:
            return None
        return self.journey[start_station]

    def journey_duration(self, start_station, end_station):
        journey_instance = [i for i in self._journey_instance(start_station) if i.end_station == end_station]
        return journey_instance[0].duration if journey_instance else None

    def build_network_from_journey(self, journeys):
        self.all_station = set()
        for journey in journeys:
            self.journey[journey.start_station].append(journey)
            self.all_station.update({journey.start_station, journey.end_station})

    def _departure_arrival_time_table(self, start_station, end_station):
        for journey in self.journey[start_station]:
            if journey.end_station == end_station:
                return journey.departure_arrival_time_table()
        return None

    def find_shortest_time_route(self, start_station, end_station):
        distances = {station: float('inf') for station in self.all_station}
        previous_stations = {station: None for station in self.all_station}
        distances[start_station] = 0
        pq = [(0, start_station)]

        while pq:
            current_distance, current_station = heapq.heappop(pq)
            if current_distance > distances[current_station]:
                continue
            for journey in self.journey[current_station]:
                neighbor = journey.end_station
                duration = convert_to_timedelta([journey.duration])[0]
                distance = current_distance + duration.total_seconds()
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_stations[neighbor] = (current_station, journey.duration)
                    heapq.heappush(pq, (distance, neighbor))

        path, total_duration = [], timedelta(seconds=distances[end_station])
        current = end_station
        while previous_stations[current]:
            prev_station, journey_duration = previous_stations[current]
            path.insert(0, current)
            current = prev_station
        if path:
            path.insert(0, start_station)

        return '-'.join(path), str(timedelta(seconds=int(total_duration.total_seconds())))

    def find_route(self, start_station, end_station):
        if start_station not in self.all_station or end_station not in self.all_station:
            raise InvalidStation(f"Invalid stations: {start_station}, {end_station}")
        return self.find_shortest_time_route(start_station, end_station)

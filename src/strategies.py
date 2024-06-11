"""
This module contains the constants used in the application.
"""
from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def find_route(self, train_network, start_station, end_station):
        pass


class ShortestTimeStrategy(RouteStrategy):
    def find_route(self, train_network, start_station, end_station):
        return train_network.find_shortest_time_route(start_station, end_station)

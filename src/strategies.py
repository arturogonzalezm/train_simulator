"""
This module contains the strategy classes used for finding routes in the Train Network application.
"""

from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    """
    Abstract base class for route finding strategies.
    """

    @abstractmethod
    def find_route(self, train_network, start_station, end_station):
        """
        Find the route between start_station and end_station using a specific strategy.
        :param train_network: The train network to find routes in.
        :param start_station: The starting station.
        :param end_station: The destination station.
        :return: The route and its duration.
        """
        pass


class ShortestTimeStrategy(RouteStrategy):
    """
    Strategy for finding the shortest time route in the train network.
    """

    def find_route(self, train_network, start_station, end_station):
        """
        Find the shortest time route between start_station and end_station.
        :param train_network: The train network to find routes in.
        :param start_station: The starting station.
        :param end_station: The destination station.
        :return: The route and its duration.
        """
        return train_network.find_shortest_time_route(start_station, end_station)

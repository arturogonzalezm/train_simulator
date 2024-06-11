"""
This module initializes the Train Network and finds the shortest route from city A to city E using
a given timetable and journey durations.
"""

import datetime
import csv
from src.logger import logger
from src.journey import Journey
from src.network import TrainNetwork


def load_routes_from_csv(file_path):
    """
    Load routes from a CSV file and create Journey instances.
    :param file_path: The path to the CSV file containing route information.
    :return: A list of Journey instances.
    """
    routes = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start_station = row['start_station'].strip()
            end_station = row['end_station'].strip()
            departure_times = row['departure_times'].strip().replace('"', '').split()
            duration = row['duration'].strip()
            route_timetable = {
                'departure_time': departure_times,
                'duration': duration
            }
            journey = Journey(start_station, end_station)
            journey.timetable = route_timetable
            routes.append(journey)
    return routes


def run(file_path):
    """
    Initialize the Train Network, build the network from the given routes, and find the shortest route
    from city A to city E.
    :param file_path: The path to the CSV file containing route information.
    :return: None
    """
    logger.info('%s Initialising Train Network %s', '*' * 10, '*' * 10)

    routes = load_routes_from_csv(file_path)

    start_time = datetime.datetime.now()
    train_network = TrainNetwork()
    train_network.build_network_from_journey(routes)
    quickest_route = train_network.find_route('A', 'E')
    finish_time = datetime.datetime.now()

    if not quickest_route:
        logger.info('No journey available from A to E in %s, please check timetable is correct', file_path)
    else:
        logger.info('The quickest route in %s is %s, duration %s', file_path, quickest_route[0], quickest_route[1])

    logger.info('Time taken for %s: %s', file_path, finish_time - start_time)


if __name__ == '__main__':
    FILE_PATH = 'data/routes_0.csv'  # File path to the specific CSV file
    run(FILE_PATH)

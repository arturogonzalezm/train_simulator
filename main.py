import datetime
import csv

from src.logger import logger
from src.journey import Journey
from src.network import TrainNetwork


def load_routes_from_csv(file_path):
    routes = []
    with open(file_path, mode='r') as csvfile:
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
    logger.info('*' * 10 + ' Initialising Train Network ' + '*' * 10)

    routes = load_routes_from_csv(file_path)

    start_time = datetime.datetime.now()
    train_network = TrainNetwork()
    train_network.build_network_from_journey(routes)
    quickest_route = train_network.find_route('A', 'E')
    finish_time = datetime.datetime.now()

    if not quickest_route:
        logger.info(f'No journey available from A to E in {file_path}, please check timetable is correct')
    else:
        logger.info(f'The quickest route in {file_path} is {quickest_route[0]}, duration {quickest_route[1]}')

    logger.info(f'Time taken for {file_path}: {finish_time - start_time}\n')


if __name__ == '__main__':
    file_path = 'data/routes_0.csv'  # File path to the specific CSV file
    run(file_path)

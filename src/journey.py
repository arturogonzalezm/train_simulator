"""
This module contains the constants used in the application.
"""
from datetime import datetime, timedelta

from src.exceptions import InvalidTimeFormat, InvalidTimeTable
from src.utils import verify_time_format


class Journey:
    def __init__(self, start_station, end_station):
        self._start_station = start_station
        self._end_station = end_station
        self._timetable = {}
        self._departure_time = None

    @property
    def timetable(self):
        return self._timetable

    @timetable.setter
    def timetable(self, time_table):
        self._timetable = self._uniformat_timetable(time_table)

    @property
    def duration(self):
        return self._timetable['duration']

    @property
    def start_station(self):
        return self._start_station

    @property
    def end_station(self):
        return self._end_station

    @property
    def departure_time(self):
        if self._departure_time is None:
            self._departure_time = self._extract_departure_time()
        return self._departure_time

    def arrival_time(self, departure_time):
        if departure_time not in self._timetable.get('departure_time'):
            return
        duration = self._timetable['duration']
        departure_time_stamp = datetime.strptime(departure_time, '%H:%M')
        duration_hour, duration_min = duration.split(':')
        duration_time_stamp = timedelta(hours=int(duration_hour), minutes=int(duration_min))
        arrival_time = (departure_time_stamp + duration_time_stamp).strftime('%H:%M')
        return datetime.strptime(arrival_time, '%H:%M')

    def _extract_departure_time(self):
        return self._timetable['departure_time']

    def departure_arrival_time_table(self):
        time_table = [(departure_time, self.arrival_time(departure_time).strftime('%H:%M'))
                      for departure_time in self.departure_time]
        return time_table

    @staticmethod
    def _uniform_time_format(time_str):
        if not time_str or not verify_time_format(time_str):
            return None

        hour, minute = time_str.split(':')
        new_format = ['0' + i if len(i) == 1 else i for i in [hour, minute]]
        return ':'.join(new_format)

    def _uniformat_timetable(self, time_table):
        sanitized_time_format = []
        if time_table.get('departure_time') and time_table.get('duration'):
            for time_stamp in time_table['departure_time']:
                if isinstance(time_stamp, str):
                    sanitized_time_ = self._uniform_time_format(time_stamp)
                    if sanitized_time_:
                        sanitized_time_format.append(sanitized_time_)
                    else:
                        raise InvalidTimeFormat
                else:
                    raise InvalidTimeFormat
            time_table['departure_time'] = sanitized_time_format
            return time_table
        else:
            raise InvalidTimeTable

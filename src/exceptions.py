"""
This module contains the constants used in the application.
"""


class InvalidTimeFormat(Exception):
    """
    Exception raised for invalid time format.
    :param code: Error code.
    :param message: Error message.
    """
    code = 7
    message = 'Invalid time format. Should be %H:%M'

    def __str__(self):
        return self.message


class InvalidTimeTable(Exception):
    """
    Exception raised for invalid time table format.
    :param code: Error code.
    :param message: Error message.
    """
    code = 10
    message = "Invalid time table. Should be {'departure_time': list of time str, 'duration': int}"

    def __str__(self):
        return self.message


class InvalidNetwork(Exception):
    """
    Exception raised when the network cannot be built.
    :param code: Error code.
    :param message: Error message.
    """
    code = 15
    message = "Fail to build network."

    def __str__(self):
        return self.message


class InvalidStation(Exception):
    """
    Exception raised when a station is not in the network.
    :param code: Error code.
    :param message: Error message.
    """
    code = 15
    message = "Station is not in the network."

    def __str__(self):
        return self.message


class NoTimetableAvailable(Exception):
    """
    Exception raised when no valid timetable can be extracted.
    :param code: Error code.
    :param message: Error message.
    """
    code = 20
    message = "Couldn't extract a valid time table from the journey."

    def __str__(self):
        return self.message

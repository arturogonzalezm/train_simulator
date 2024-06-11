"""
This module contains the tests for the utility functions in the utils.py module.
"""
import pytest
from datetime import datetime, timedelta
from src.utils import (
    convert_to_datetime, convert_to_timedelta, sort_time,
    verify_time_format, verify_duration, verify_departure_time
)
from src.exceptions import InvalidTimeFormat


def test_convert_to_datetime():
    """
    Test the convert_to_datetime function.
    :return:
    """
    assert convert_to_datetime(["08:00", "12:00"]) == [datetime.strptime("08:00", '%H:%M'),
                                                       datetime.strptime("12:00", '%H:%M')]
    assert convert_to_datetime([datetime.strptime("08:00", '%H:%M'), datetime.strptime("12:00", '%H:%M')]) == [
        datetime.strptime("08:00", '%H:%M'), datetime.strptime("12:00", '%H:%M')]

    with pytest.raises(InvalidTimeFormat):
        convert_to_datetime(["invalid", "12:00"])

    with pytest.raises(InvalidTimeFormat):
        convert_to_datetime([800, "12:00"])


def test_convert_to_timedelta():
    """
    Test the convert_to_timedelta function.
    :return:
    """
    assert convert_to_timedelta(["01:00", "02:30"]) == [timedelta(hours=1), timedelta(hours=2, minutes=30)]
    assert convert_to_timedelta([timedelta(hours=1), timedelta(hours=2, minutes=30)]) == [timedelta(hours=1),
                                                                                          timedelta(hours=2,
                                                                                                    minutes=30)]

    with pytest.raises(InvalidTimeFormat):
        convert_to_timedelta(["invalid", "02:30"])

    with pytest.raises(InvalidTimeFormat):
        convert_to_timedelta([timedelta(hours=1), 230])


def test_sort_time():
    """
    Test the sort_time function.
    :return:
    """
    assert sort_time(["12:00", "08:00", "16:00"]) == [datetime.strptime("08:00", '%H:%M'),
                                                      datetime.strptime("12:00", '%H:%M'),
                                                      datetime.strptime("16:00", '%H:%M')]
    assert sort_time([datetime.strptime("12:00", '%H:%M'), datetime.strptime("08:00", '%H:%M'),
                      datetime.strptime("16:00", '%H:%M')]) == [datetime.strptime("08:00", '%H:%M'),
                                                                datetime.strptime("12:00", '%H:%M'),
                                                                datetime.strptime("16:00", '%H:%M')]


def test_verify_time_format():
    """
    Test the verify_time_format function.
    :return:
    """
    assert verify_time_format("08:00") is True
    assert verify_time_format("23:59") is True
    assert verify_time_format("24:00") is False
    assert verify_time_format("12:60") is False
    assert verify_time_format("invalid") is False
    assert verify_time_format(800) is False


def test_verify_duration():
    """
    Test the verify_duration function.
    :return:
    """
    assert verify_duration("1:30") is True
    assert verify_duration("10:59") is True
    assert verify_duration("0:60") is False
    assert verify_duration("-1:00") is False
    assert verify_duration("0:00") is False
    assert verify_duration("invalid") is False
    assert verify_duration(130) is False


def test_verify_departure_time():
    """
    Test the verify_departure_time function.
    :return:
    """
    assert verify_departure_time("08:00 12:00 16:00") is True
    assert verify_departure_time("08:00 invalid 16:00") is False
    assert verify_departure_time("24:00") is False
    assert verify_departure_time("") is True

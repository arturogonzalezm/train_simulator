"""
Test cases for the exceptions module.
"""
import pytest

from src.exceptions import (
    InvalidTimeFormat, InvalidTimeTable, InvalidNetwork, InvalidStation, NoTimetableAvailable
)


def test_invalid_time_format():
    """
    Test the InvalidTimeFormat exception.
    :return: None
    """
    with pytest.raises(InvalidTimeFormat) as exc_info:
        raise InvalidTimeFormat()
    assert exc_info.value.code == 7
    assert str(exc_info.value) == InvalidTimeFormat.message


def test_invalid_time_table():
    """
    Test the InvalidTimeTable exception.
    :return:
    """
    with pytest.raises(InvalidTimeTable) as exc_info:
        raise InvalidTimeTable()
    assert exc_info.value.code == 10
    assert str(exc_info.value) == InvalidTimeTable.message


def test_invalid_network():
    """
    Test the InvalidNetwork exception.
    :return:
    """
    with pytest.raises(InvalidNetwork) as exc_info:
        raise InvalidNetwork()
    assert exc_info.value.code == 15
    assert str(exc_info.value) == InvalidNetwork.message


def test_invalid_station():
    """
    Test the InvalidStation exception.
    :return:
    """
    with pytest.raises(InvalidStation) as exc_info:
        raise InvalidStation()
    assert exc_info.value.code == 15
    assert str(exc_info.value) == InvalidStation.message


def test_no_timetable_available():
    """
    Test the NoTimetableAvailable exception.
    :return:
    """
    with pytest.raises(NoTimetableAvailable) as exc_info:
        raise NoTimetableAvailable()
    assert exc_info.value.code == 20
    assert str(exc_info.value) == NoTimetableAvailable.message

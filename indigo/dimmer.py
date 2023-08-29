from __future__ import annotations
from typing import TYPE_CHECKING

import indigo

if TYPE_CHECKING:
    import _types


def allLightsOff(selector: indigo.kAllDeviceSel = None) -> None:
    """
    Turns off all dimmers.

    :param selector: The selector to use when turning off the dimmers. If None, all dimmers will be turned off.
    :return: None
    """
    ...


def allLightsOn(selector: indigo.kAllDeviceSel = None) -> None:
    """
    Turns on all dimmers.

    :param selector: The selector to use when turning on the dimmers. If None, all dimmers will be turned on.
    :return: None
    """
    ...


def brighten(device: _types.dimmerDeviceType, by: int = -1, delay: int = -1):
    """
    Brightens a dimmer by the specified amount.

    :param device: The device to brighten.
    :param by: Not required. The amount to brighten the device by. This is a value between 0 and 100.
    :param delay: Not required. The amount of time to wait between increments.
    :return: None
    """
    ...


def dim(device: _types.dimmerDeviceType, by: int = -1, delay: int = -1):
    """
    Dims a dimmer by the specified amount.

    :param device: The device to dim.
    :param by: Not required. The amount to dim the device by. This is a value between 0 and 100.
    :param delay: Not required. The amount of time to wait between increments.
    :return: None
    """
    ...


def setBrightness(device: _types.dimmerDeviceType, *, value: int, delay: int = -1):
    """
    Sets the brightness of a dimmer.

    :param device: The device to set the brightness of.
    :param value: Required. The brightness to set the device to. This is a value between 0 and 100.
    :param delay: The amount of seconds to wait before setting the brightness.
    :return: None
    """
    ...


def setLedState(device: _types.dimmerDeviceType, *, index: int, value: bool, suppressLogging: bool = False, updateStatesOnly: bool = False):
    """
    Sets the state of a dimmer's LED.

    :param device: The device to set the LED state of.
    :param index: The index of the LED to set the state of.
    :param value: The state to set the LED to. True is on, False is off.
    :param suppressLogging: If True, the state change will not be logged.
    :param updateStatesOnly: If True, the state change will not be sent to the device.
    :return: None
    """
    ...

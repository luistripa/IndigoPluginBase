from typing import Union

from .._objects import Trigger


def delete(id: Union[int, Trigger]):
    pass


def duplicate(id: Union[int, Trigger]) -> Trigger:
    pass


def enable(id: Union[int, Trigger], value: bool = True, duration: int = None, delay: int = None):
    pass


def execute(id: Union[int, Trigger], ignoreConditions: bool = True):
    pass


def moveToFolder(id: Union[int, Trigger], value: int):
    pass


def removeDelayedActions(id: Union[int, Trigger]):
    pass

from typing import Union

import indigo


def delete(id: Union[int, indigo.Trigger]):
    pass


def duplicate(id: Union[int, indigo.Trigger]) -> indigo.Trigger:
    pass


def enable(id: Union[int, indigo.Trigger], value: bool = True, duration: int = None, delay: int = None):
    pass


def execute(id: Union[int, indigo.Trigger], ignoreConditions: bool = True):
    pass


def moveToFolder(id: Union[int, indigo.Trigger], value: int):
    pass

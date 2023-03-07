
import typing as _typing

from .._objects import *


def create(name: str, value: str = None, folder: _typing.Union[str, int, Folder] = None) -> Variable:
    """
    Creates a new variable.
    :param name: The name of the variable.
    :param value: The value of the variable.
    :param folder: The folder to create the variable in.
    :return: The new variable instance
    """
    return None  # TODO


def delete(variable: _typing.Union[str, int, Variable]) -> None:
    """
    Deletes a variable.
    :param variable: The variable to delete.
    :return: None
    """
    pass


def duplicate(variable: _typing.Union[str, int, Variable], duplicateName: str = None):
    """
    Duplicates a variable.
    :param variable: The variable to duplicate.
    :param duplicateName: The name of the duplicate variable.
    :return: The new variable instance
    """
    pass


def updateValue(variable: _typing.Union[str, int, Variable], value: str) -> None:
    """
    Updates the value of a variable.
    :param variable: The variable to update.
    :param value: The new value of the variable.
    :return: None
    """
    pass

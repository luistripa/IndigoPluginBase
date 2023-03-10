import indigo
from typing import Union


def create(name: str, value: str = None, folder: Union[str, int, indigo.Folder] = None) -> indigo.Variable:
    """
    Creates a new variable.
    :param name: The name of the variable.
    :param value: The value of the variable.
    :param folder: The folder to create the variable in.
    :return: The new variable instance
    """
    return None


def delete(variable: Union[str, int, indigo.Variable]) -> None:
    """
    Deletes a variable.
    :param variable: The variable to delete.
    :return: None
    """
    pass


def duplicate(variable: Union[str, int, indigo.Variable], duplicateName: str = None):
    """
    Duplicates a variable.
    :param variable: The variable to duplicate.
    :param duplicateName: The name of the duplicate variable.
    :return: The new variable instance
    """
    pass


def updateValue(variable: Union[str, int, indigo.Variable], value: str) -> None:
    """
    Updates the value of a variable.
    :param variable: The variable to update.
    :param value: The new value of the variable.
    :return: None
    """
    pass

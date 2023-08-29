from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import indigo

if TYPE_CHECKING:
    import _types


def create(name: str, *, value: str = None, folder: Optional[_types.folderType] = None) -> indigo.Variable:
    """
    Creates a new variable.
    :param name: The name of the variable.
    :param value: The value of the variable.
    :param folder: The folder to create the variable in.
    :return: The new variable instance
    """
    ...


def delete(id: _types.variableType) -> None:
    """
    Deletes a variable.
    :param id: The variable to delete.
    :return: None
    """
    ...


def duplicate(id: _types.variableType, duplicateName: str = None) -> indigo.Variable:
    """
    Duplicates a variable.
    :param id: The variable to duplicate.
    :param duplicateName: The name of the duplicate variable.
    :return: The new variable instance
    """
    ...


def getDependencies(id: _types.variableType) -> dict:
    # TODO: docstring here
    ...


def moveToFolder(id: _types.variableType, *, value: Optional[_types.folderType]) -> None:
    """
    Moves a variable to a new folder.
    :param variable: ID or instance of the variable to move.
    :param value: ID or instance of the folder to move the variable to.
    :return: None
    """
    ...


def displayInRemoteUI(id: _types.variableType, *, value: bool) -> None:
    """
    Sets whether a variable is displayed in the remote UI.
    :param id: ID or instance of the variable to be displayed.
    :param value: Whether the variable should be displayed in the remote UI.
    :return: None
    """
    ...

def updateValue(id: _types.variableType, *, value: str) -> None:
    """
    Updates the value of a variable.
    :param id: The variable to update.
    :param value: The new value of the variable.
    :return: None
    """
    ...

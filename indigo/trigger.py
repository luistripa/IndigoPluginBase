from __future__ import annotations

from typing import Union, TYPE_CHECKING

import indigo

if TYPE_CHECKING:
    import _types


def delete(id: _types.triggerType):
    """Delete the specified trigger regardless of its type.

    :param id: ID or instance of the trigger to delete.
    """
    ...


def duplicate(id: _types.triggerType, duplicateName: Union[str, None] = None) -> indigo.Trigger:
    """Duplicate the specified trigger regardless of its type.
    
    This method returns a copy of the new trigger.

    :param id: ID or instance of the trigger to duplicate.
    :param duplicateName: Optional name for the new trigger.
    """
    ...


def enable(id: _types.triggerType, *, value: bool, duration: Union[int, None] = None, delay: Union[int, None] = None):
    """Enables or disables the trigger, optionally delaying for some period of time and optionally toggling back after the given period.
    
    :param id: ID or instance of the trigger to enable or disable.
    :param value: True to enable, False to disable.
    :param duration: Optional duration before the trigger is switched back to its original state.
    :param delay: Optional delay before the trigger is enabled/disabled.
    """   
    ...


def execute(id: _types.triggerType, ignoreConditions: bool = False):
    """Tell the indigo server to execute the actions associated with the trigger.
    
    If trigger belongs to a plugin, this is the method you want to call when all conditions are met fo a specific event.
    If you're calling this way, make sure ignoreConditions is set to False so that any conditions associated with the trigger inside indigo are checked.
    
    :param id: ID or instance of the trigger to execute.
    :param ignoreConditions: If True, the conditions associated with the trigger will be ignored."""
    ...


def moveToFolder(id: _types.triggerType, *, value: _types.folderType):
    """Moves the specified trigger to the specified folder.
    
    You can get a list of folders by using indigo.triggers.folders, which will return a dictionary.
    The key is the folder id and the value is the folder name.
    
    :param id: ID or instance of the trigger to move.
    :param value: ID or instance of the folder to move the trigger to."""
    ...


def removeDelayedActions(id: _types.triggerType):
    """Removes any delayed actions associated with the trigger.
    
    :param id: ID or instance of the trigger to remove delayed actions from."""
    ...

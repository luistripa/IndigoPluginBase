from typing import Union

import indigo


def delete(id: Union[int, indigo.Trigger]):
    """Delete the specified trigger regardless of it's type.

    :param id: Id or instance of the trigger to delete.
    """
    pass


def duplicate(id: Union[int, indigo.Trigger], duplicateName: str = None) -> indigo.Trigger:
    """Duplicate the specified trigger regardless of it's type.
    
    This method returns a copy of the new trigger.

    :param id: Id or instance of the trigger to duplicate.
    :param duplicateName: Optional name for the new trigger.
    """
    pass


def enable(id: Union[int, indigo.Trigger], value: bool = True, duration: int = None, delay: int = None):
    """Enables or disables the trigger, optionally delaying for some period of time and optionally toggling back after the given period.
    
    :param id: Id or instance of the trigger to enable or disable.
    :param value: True to enable, False to disable.
    :param duration: Optional duration before the trigger is switched back to it's original state.
    :param delay: Optional delay before the trigger is enabled/disabled.
    """   
    pass


def execute(id: Union[int, indigo.Trigger], ignoreConditions: bool = False):
    """Tell the indigo server to exexcute the actions associated with the trigger.
    
    If trigger belongs to a plugin, this is the method you want to call when all conditions are met fo a specific event.
    If you're calling this way, make sure ignoreConditions is set to False so that any conditions associated with the trigger inside indigo are checked.
    
    :param id: Id or instance of the trigger to execute.
    :param ignoreConditions: If True, the conditions associated with the trigger will be ignored."""
    pass


def moveToFolder(id: Union[int, indigo.Trigger], value: int):
    """Moves the specified trigger to the specified folder.
    
    You can get a list of folders by using indigo.triggers.folders, which will return a dictionary.
    The key is the folder id and the value is the folder name.
    
    :param id: Id or instance of the trigger to move.
    :param value: Id or instance of the folder to move the trigger to."""
    pass


def removeDelayedActions(id: Union[int, indigo.Trigger]):
    """Removes any delayed actions associated with the trigger.
    
    :param id: Id or instance of the trigger to remove delayed actions from."""
    pass

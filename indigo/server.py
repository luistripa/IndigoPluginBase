import indigo
from typing import List


def log(message, type="Indigo Interacive Shell"):
    """
    Logs a message to the Indigo server log.
    :param message: The message to log.
    :param type: The message title
    :return: None
    """
    pass


def getPluginList() -> List[indigo.Plugin]:  # TODO: Is there a Plugin class in indigo package?
    return []


def getPlugin(pluginId: str) -> indigo.Plugin:
    pass

import indigo


address: str = "localhost"
apiVersion: str = "3.2"
connectionGood: bool = True
licenseStatus: indigo.kLicenseStatus = indigo.kLicenseStatus.ActiveSubscription
portNum: int = 1176
version: str = "2022.2.0"


def log(message, type="Indigo Interacive Shell"):
    """
    Logs a message to the Indigo server log.
    :param message: The message to log.
    :param type: The message title
    :return: None
    """
    pass


def getPluginList() -> list[indigo.PluginInfo]:
    return []


def getPlugin(pluginId: str) -> indigo.PluginInfo:
    pass

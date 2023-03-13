import logging
from typing import Union, Any

import indigo

import datetime


address: str = "localhost"
apiVersion: str = "3.2"
connectionGood: bool = True
licenseStatus: indigo.kLicenseStatus = indigo.kLicenseStatus.ActiveSubscription
portNum: int = 1176
version: str = "2022.2.0"


def log(message, type="Indigo Interacive Shell", level: int = logging.INFO, isError: bool = False):
    """
    Logs a message to the Indigo server log.
    :param message: The message to log.
    :param type: The message title
    :param level: The log level to use. Defaults to INFO.
    :param isError: If true, the message will be logged as an error and displayed with red text in the log console.
    :return: None
    """
    pass


def getPluginList() -> list[indigo.PluginInfo]:
    """
    Returns a list of all enable plugin object instances.

    :return: A list of all enabled plugin object instances.
    """
    return []


def getPlugin(pluginId: str) -> indigo.PluginInfo:
    """
    Returns a plugin object given the plugin id.

    :param pluginId: The plugin id of the plugin to return, such as "com.perceptiveautomation.testplugin"
    :return: The plugin object instance.
    """
    pass


def calculateSunrise(myDateObject: Union[datetime.date, None] = None) -> datetime.datetime:
    """
    Calculates the sunrise time for the given date.

    Date can be None, in which case the current date is used.

    :param myDateObject: The date to calculate the sunrise for.
    :return: The sunrise time for the given date.
    """
    pass


def calculateSunset(myDateObject: Union[datetime.date, None] = None) -> datetime.datetime:
    """
    Calculates the sunset time for the given date.

    Date can be None, in which case the current date is used.

    :param myDateObject: The date to calculate the sunset for.
    :return: The sunset time for the given date.
    """
    pass


def getEventLogList(showTimeStamp: bool = True, lineCount: int = 1500, returnAsList: bool = False) -> \
        Union[list[dict[str, Any]], str]:
    """
    Returns a string with the latest log entries. Each line is separated by a line feed character.

    When returned as a list, the individual dicts will contain the following keys:
    "Message": The log entry message
    "TypeVal": ???
    "TypeStr": The log entry type string as shown on the log console
    "Timestamp": The log entry timestamp as a datetime object

    :param showTimeStamp: Indicate whether every line should have it's time stamp preprended to the log entry.
    :param lineCount: The number of lines to return from the log entry starting from the newest and going backwards in time.
    :param returnAsList: If true a list of dicts is returned containing individual log entry attributes.
                    If false a string containing a textual description of the log lines is returned
    :return: A string containing the log entries or a list of dicts containing the log entry attributes.
    """
    pass


def getDbFilePath() -> str:
    """
    Returns the POSIX path to the current database file (includes the file name with extension).

    :return: The path to the Indigo database file.
    """
    pass


def getInstallFolderPath() -> str:
    """
    Returns the POSIX path to the current Indigo installation path.
    Useful if you want to manipulate files (like graphics and scripts) that are in the Indigo installation path.

    :return: The path to the Indigo installation folder.
    """
    pass


def getLatitudeAndLongitude() -> tuple[float, float]:
    """
    Returns a list of floating point numbers where the first float is the latitude and the second (and last) is the longitude.

    :return: A tuple containing the latitude and longitude of the current Indigo location.
    """
    pass


def getReflectorURL() -> Union[str, None]:
    """
    Returns the URL of the Indigo reflector server.
    
    :return: The URL of the Indigo reflector server or None if there is no reflector or the remote access is disabled.
    """
    pass


def getSerialPorts(filter: Union[str, None] = None) -> list[str]:
    """
    Returns a list of serial ports that are available on the system.

    :param filter: If specified, only serial ports that contain the filter string will be returned. Currently only
                      "indigo.ignoreBluetooth" is supported.
    :return:
    """
    pass


def getTime() -> datetime.datetime:
    """
    Returns the current Indigo server time as a datetime object.

    :return: The current Indigo server time as a datetime object.
    """
    pass


def getWebServerURL() -> str:
    """
    Returns the URL that best represents the Indigo web server.

    The order of preference is:
    1. The reflector URL if it is available, e.g.: https://myreflector.indigodomo.com
    2. The Bonjour URL if it is available, e.g.: https://myindigo.local:PORT
    3. The local IP address URL, e.g.: http://localhost:PORT

    :return: The URL of the Indigo web server.
    """
    pass


def removeAllDelayedActions():
    """
    This command will remove all delayed actions currently scheduled.

    :return: None
    """
    pass


def sendEmailTo(address: str, subject: str = "", body: str = ""):
    """
    Sends an email to the specified address.

    :param address: The email addresses to send the email to separated by semicolons.
    :param subject: The subject of the email.
    :param body: The body of the email.
    :return: None
    """
    pass


def speak(text: str, waitUntilDone: bool = False):
    """
    Speak a text string using the built-in speech synthesizer.

    :param text: The text to speak.
    :param waitUntilDone: If true, the command will not return until the text has been spoken.
    # TODO: waitUntilDone default value?
    :return: None
    """
    pass

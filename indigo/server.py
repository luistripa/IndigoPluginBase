from __future__ import annotations
import logging
from typing import Union, Any, Callable, Optional

import indigo

import datetime


address: str
apiVersion: str
connectionGood: bool
licenseStatus: indigo.kLicenseStatus
portNum: int
version: str


def log(message: Any, type: str = "Indigo Interacive Shell", level: int = logging.INFO, isError: bool = False):
    """
    Logs a message to the Indigo server log.
    :param message: The message to log.
    :param type: The message title
    :param level: The log level to use. Defaults to INFO.
    :param isError: If true, the message will be logged as an error and displayed with red text in the log console.
    :return: None
    """
    ...


def getPluginList() -> list[indigo.PluginInfo]:
    """
    Returns a list of all enable plugin object instances.

    :return: A list of all enabled plugin object instances.
    """
    ...


def getPlugin(pluginId: str) -> indigo.PluginInfo:
    """
    Returns a plugin object given the plugin id.

    :param pluginId: The plugin id of the plugin to return, such as "com.perceptiveautomation.testplugin"
    :return: The plugin object instance.
    """
    ...


def calculateSunrise(myDateObject: Optional[datetime.date] = None) -> datetime.datetime:
    """
    Calculates the sunrise time for the given date.

    Date can be None, in which case the current date is used.

    :param myDateObject: The date to calculate the sunrise for.
    :return: The sunrise time for the given date.
    """
    ...


def calculateSunset(myDateObject: Optional[datetime.date] = None) -> datetime.datetime:
    """
    Calculates the sunset time for the given date.

    Date can be None, in which case the current date is used.

    :param myDateObject: The date to calculate the sunset for.
    :return: The sunset time for the given date.
    """
    ...


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
    ...


def getDbFilePath() -> str:
    """
    Returns the POSIX path to the current database file (includes the file name with extension).

    :return: The path to the Indigo database file.
    """
    ...


def getInstallFolderPath() -> str:
    """
    Returns the POSIX path to the current Indigo installation path.
    Useful if you want to manipulate files (like graphics and scripts) that are in the Indigo installation path.

    :return: The path to the Indigo installation folder.
    """
    ...


def getLatitudeAndLongitude() -> tuple[float, float]:
    """
    Returns a list of floating point numbers where the first float is the latitude and the second (and last) is the longitude.

    :return: A tuple containing the latitude and longitude of the current Indigo location.
    """
    ...


def getReflectorURL() -> Optional[str]:
    """
    Returns the URL of the Indigo reflector server.
    
    :return: The URL of the Indigo reflector server or None if there is no reflector or the remote access is disabled.
    """
    ...


def getRelectorStatus() -> dict[str, Any]:
    """
    Returns a dict containing the status of the Indigo reflector server.
    Keys:
        licenseStatus: indigo.kLicenseStatus
        reflectorURL: str
        reflectorStatusMsg: str
    """
    ...


def getSerialPorts(filter: Optional[str] = None) -> list[str]:
    """
    Returns a list of serial ports that are available on the system.

    :param filter: If specified, only serial ports that contain the filter string will be returned. Currently only
                      "indigo.ignoreBluetooth" is supported.
    :return:
    """
    ...


def getTime() -> datetime.datetime:
    """
    Returns the current Indigo server time as a datetime object.

    :return: The current Indigo server time as a datetime object.
    """
    ...


def getWebServerURL() -> str:
    """
    Returns the URL that best represents the Indigo web server.

    The order of preference is:
    1. The reflector URL if it is available, e.g.: https://myreflector.indigodomo.com
    2. The Bonjour URL if it is available, e.g.: https://myindigo.local:PORT
    3. The local IP address URL, e.g.: http://localhost:PORT

    :return: The URL of the Indigo web server.
    """
    ...


def removeAllDelayedActions():
    """
    This command will remove all delayed actions currently scheduled.

    :return: None
    """
    ...


def sendEmailTo(address: str, subject: str = "", body: str = ""):
    """
    Sends an email to the specified address.

    :param address: The email addresses to send the email to separated by semicolons.
    :param subject: The subject of the email.
    :param body: The body of the email.
    :return: None
    """
    ...


def speak(text: str, waitUntilDone: bool = False):
    """
    Speak a text string using the built-in speech synthesizer.

    :param text: The text to speak.
    :param waitUntilDone: If true, the command will not return until the text has been spoken.
    # TODO: waitUntilDone default value?
    :return: None
    """
    ...


def broadcastToSubscribers(message_topic: str, message: Any) -> None:
    """

    Broadcasts a message to all subscribers of a specific topic, including subscribers on other plugins.

    :param message_topic: The topic of the message to broadcast.
    :type message_topic: str
    :param message: The message to broadcast. Can be a simple python object (string, list, dict, etc...). Complex objects may not work as intended.
    :type message: Any
    :return: None
    """
    ...


def subscribeToBroadcast(pluginId: str, message_topic: str, callback: Callable[[Any], None]) -> None:
    """
    Subscribes to a broadcast message topic. Broadcasters can be other plugins.

    :param pluginId: The plugin id of the plugin to subscribe to.
    :param message_topic: The topic of the message to subscribe to.
    :param callback: The callback function to call when a message is received.
    :return: None

    The callback function must have the following signature:
    def callback_func_name(self, pythonObject: Any) -> None:
    """
    ...

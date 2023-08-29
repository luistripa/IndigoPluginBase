from __future__ import annotations

from typing import Dict, Any, TYPE_CHECKING
import indigo

if TYPE_CHECKING:
    import _types


def allOff(selector: indigo.kAllDeviceSel = None):
    """
    Turns off all devices.

    Although in the indigo documentation the selector parameter is required, it's not. If you don't pass a selector,
    all devices will be turned off.

    :return: None
    """
    ...


def beep(deviceId: _types.deviceType) -> None:
    """
    Beeps the device. This is only supported by some devices.
    :param deviceId: The ID of the device to beep.
    :return: None
    """
    ...


def create(deviceTypeId: _types.deviceType,
           name: str,
           protocol: indigo.kProtocol,
           *,
           address: str = "",
           description: str = "",
           pluginId: str = "",
           props: Dict[str, Any] = None,
           folder: int = 0) -> indigo.Device:
    """
    Creates a new device.

    Required parameters:
    - device_type_id
    - name
    - protocol

    :param address: The address of the device. This is usually the IP address or MAC address of the device.
    :param description: The description of the device.
    :param device_type_id: The device type ID of the device.
    :param name: The name of the device.
    :param plugin_id: The plugin ID of the device.
    :param props: A dictionary of properties for the device.
    :param protocol: The protocol of the device.
    :param folder: The folder ID of the folder to create the device in.
    :return:
    """
    ...


def delete(device: _types.deviceType) -> None:
    """
    Deletes the device.
    :param device: The instance or id of the device to delete.
    :return: None
    """
    ...


def duplicate(device: _types.deviceType, duplicateName: str = "") -> indigo.Device:
    """
    Duplicates the device.

    :param device: The device to duplicate.
    :param duplicateName: The name of the duplicate device.
    :return:
    """
    ...


def enable(device: _types.deviceType, *, value: bool) -> None:
    """
    Enables or disables the device.
    :param device: The device to enable or disable.
    :param value: True to enable the device, False to disable it.
    :return: None
    """
    pass


def getGroupList(device: _types.deviceType) -> indigo.List:
    """
    Returns a list of devices in the same group, including the device itself.
    :param device: The device to get the group list for.
    :return: A list of devices in the same group, including the device itself.
    """
    ...


def getDependencies(device: _types.deviceType) -> indigo.Dict:
    """
    Returns a dict containing the dependencies of the device.
    Dependencies can be action groups, control pages, other devices, schedules, triggers, and variables.

    The dictionary will have 5 top-level keys: “actionGroups”, “controlPages”, “devices”, “schedules”, “triggers”, and “variables”.
    Each one of those keys will return a list object.
    Inside that list object will be multiple dicts, one for each dependency (or an empty list if there are none).
    Each dependency dictionary has two keys: “ID” which is the unique id and “Name” which is the name of the object.

    :see: https://wiki.indigodomo.com/doku.php?id=indigo_2021.1_documentation:device_class#get_dependencies

    :param device: The device to get the dependencies for.
    :return: A dict containing the dependencies of the device.
    """
    ...


def moveToFolder(device: _types.deviceType, *, value: _types.folderType):
    """
    Moves the device to the specified folder.
    :param device:
    :param folder:
    :return:
    """
    ...


def ping(device: _types.deviceType, suppressLogging: bool = False) -> bool:
    """
    Pings the device.
    :param device: The device to ping.
    :param suppressLogging: True to suppress logging, False to log.
    :return: A dict containing the "Success" and "TimeDelta" (milliseconds) result.
    """
    ...


def removeDelayedActions(device: _types.deviceType) -> None:
    """
    Removes all delayed actions for the device.
    :param device: The device to remove the delayed actions for.
    :return: None
    """
    ...


def resetEnergyAccumTotal(device: _types.deviceType) -> None:
    """
    Resets the energy accumulation total for the device.
    :param device: The device to reset the energy accumulation total for.
    :return: None
    """
    ...


def displayInRemoteUI(device: _types.deviceType, *, value: bool) -> None:
    """
    Sets whether the device should be displayed in the remote UI.
    :param device: The device to set the display in remote UI value for.
    :param value: True to display the device in the remote UI, False to hide it.
    :return: None
    """
    ...


def statusRequest(device: _types.deviceType, suppressLogging: bool = False) -> None:
    """
    Requests the device to send its current status to the server.
    :param device: The device to request the status for.
    :param suppressLogging: True to suppress logging, False to log.
    :return: None
    """
    ...


def toggle(device: _types.deviceType, delay: int = 0, duration: int = 0) -> None:
    """
    Toggles the device.
    :param device: The device to toggle.
    :param delay: The delay in seconds before the device is toggled.
    :param duration: The duration in seconds before the device is toggled back to its original state.
    :return: None
    """
    ...


def turnOff(device: _types.deviceType, delay: int = 0, duration: int = 0) -> None:
    """
    Turns off the device.
    Only works for devices that can be turned on and off.

    :param device: The device to turn off.
    :param delay: The delay in seconds before the device is turned off.
    :param duration: The duration in seconds before the device is turned back on.
    :return: None
    """
    ...


def turnOn(device: _types.deviceType, delay: int = 0, duration: int = 0) -> None:
    """
    Turns on the device.
    Only works for devices that can be turned on and off.

    :param device: The device to turn on.
    :param delay: The delay in seconds before the device is turned on.
    :param duration: The duration in seconds before the device is turned off.
    :return: None
    """
    ...


def unlock(device: _types.deviceType, delay: int = 0, duration: int = 0) -> None:
    """
    Unlocks the device.
    Only works for devices that can be locked and unlocked.

    :param device: The device to unlock.
    :param delay: The delay in seconds before the device is unlocked.
    :param duration: The duration in seconds before the device is locked.
    :return: None
    """
    ...


def lock(device: _types.deviceType, delay: int = 0, duration: int = 0) -> None:
    """
    Locks the device.
    Only works for devices that can be locked and unlocked.

    :param device: The device to lock.
    :param delay: The delay in seconds before the device is locked.
    :param duration: The duration in seconds before the device is unlocked.
    :return: None
    """
    ...

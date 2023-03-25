import dataclasses
import datetime
from typing import List, Dict, Any

import indigo


class DeviceList(indigo.List):

    folders: indigo.FolderList = None
    folder: indigo.FolderCmds = None

    def subscribeToChanges(self):
        """
        Must only be used inside plugins.

        Subscribes to device changes. This includes state and property changes.

        Every time a device changes, the plugin handler will call the deviceUpdated method.

        :return: None
        """
        pass

    def __iter__(self, filter="") -> List["indigo.Device"]:
        pass


@dataclasses.dataclass
class Device:

    # See https://wiki.indigodomo.com/doku.php?id=indigo_2021.1_documentation:device_class#device_base_class_properties
    address: str
    batteryLevel: int  # None if the device doesn't have a battery
    buttonGroupCount: int
    configured: bool
    description: str
    deviceTypeId: str
    displayStateId: str
    displayStateValRaw: Any
    displayStateImageSel: indigo.kStateImageSel
    enabled: bool
    energyCurLevel: float
    energyAccumTotal: float
    energyAccumBaseTime: datetime.datetime
    energyAccumTimeDelta: int
    errorState: str
    folderId: int
    globalProps: Dict[str, Any]
    id: int
    lastChanged: datetime.datetime
    model: str
    name: str
    ownerProps: Dict[str, Any]
    pluginId: str
    pluginProps: Dict[str, Any]
    protocol: indigo.kProtocol
    remoteDisplay: bool
    sharedProps: Dict[str, Any]
    states: Dict[str, Any]
    supportsAllLightsOnOff: bool
    supportsAllOff: bool
    supportsOnState: bool
    supportsStatusRequest: bool


    def refreshFromServer(self) -> None:
        """
        Refreshes the device from the server. This is useful if you have changed the device on the server and want to
        update the local copy.
        :return: None
        """
        pass

    def updateStateOnServer(self, key: str, value: Any) -> None:
        """
        Updates a single state on the server.
        :param key: The name of the state to update.
        :param value: The value to set the state to.
        :return: None
        """
        pass

    def updateStatesOnServer(self, states: List[Dict[str, Any]]) -> None:
        """
        Updates multiple states on the server. This is more efficient than calling updateStateOnServer() multiple times.
        :param states: A list of dictionaries, each containing a 'key' and 'value' key. The 'key' is the name of the state
        to update, and the 'value' is the value to set the state to.
        :return: None
        """
        pass

    def updateStateImageOnServer(self, image: str) -> None:
        """
        Updates the state image on the server.
        :param image:
        :return:
        """
        pass


class DimmerDevice(Device):
    """
    See https://wiki.indigodomo.com/doku.php?id=indigo_2021.1_documentation:device_class#dimmerdevice

    This device type offers two states: 'onOffState' and 'brightnessLevel'.

    The 'onOffState' state is a boolean value that indicates whether the device is on or off.

    The 'brightnessLevel' state is an integer value that indicates the brightness level of the device. This value is
    between 0 and 100 and can be accessed by dev.brightness
    """

    brightness: int
    ledStates: List[bool]
    onState: bool  # Indicates whether the device is on. Shortcut for self.states['onOffState']

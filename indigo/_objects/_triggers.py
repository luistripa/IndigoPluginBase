from typing import List

from ._actions import Action
from indigo._utils import Dict

from .._enums._triggers import *


__all__ = [
    'Trigger',
    'DeviceStateChangeTrigger',
]


class Trigger:
    actions: List[Action]
    description: str
    enabled: bool
    folderId: int
    globalProps: Dict
    id: int
    name: str
    pluginProps: Dict
    suppressLogging: bool
    upload: bool  # True if IndigoServer should attempt to upload the trigger to the interface - will always be False for plugin triggers

    def replaceOnServer(self):
        pass


class DeviceStateChangeTrigger(Trigger):
    deviceId: int
    stateChangeType: kStateChange
    stateSelector: kStateSelector
    stateSelectorIndex: int
    stateValue: str


class EmailReceivedTrigger(Trigger):
    emailFilter: kEmailFilter
    emailFrom: str
    emailSubject: str

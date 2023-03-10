import indigo
from typing import List


class TriggerList(indigo.List):

    def __iter__(self, filter="") -> List["indigo.Trigger"]:
        pass


class Trigger:
    actions: List[indigo.BaseAction]
    description: str
    enabled: bool
    folderId: int
    globalProps: indigo.Dict
    id: int
    name: str
    pluginProps: indigo.Dict
    suppressLogging: bool
    upload: bool  # True if IndigoServer should attempt to upload the trigger to the interface - will always be False for plugin triggers

    def replaceOnServer(self):
        pass


class DeviceStateChangeTrigger(Trigger):
    deviceId: int
    stateChangeType: indigo.kStateChange
    stateSelector: indigo.kStateSelector
    stateSelectorIndex: int
    stateValue: str


class EmailReceivedTrigger(Trigger):
    emailFilter: indigo.kEmailFilter
    emailFrom: str
    emailSubject: str

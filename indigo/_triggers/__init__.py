from __future__ import annotations

from typing import List

import indigo


class TriggerList(indigo.List):

    folders: indigo.FolderList
    folder: indigo.FolderCmds

    def __iter__(self, filter="") -> List["indigo.Trigger"]: ...


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

    def replaceOnServer(self): ...


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

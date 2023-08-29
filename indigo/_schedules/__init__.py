from __future__ import annotations

import dataclasses
import datetime
from typing import List, Dict, Any

import indigo


class ScheduleList(indigo.List):
    
    folders: indigo.FolderList
    folder: indigo.FolderCmds

    # TODO: Missing methods: 'get', 'getId', 'getName', 'has_key', 'iter', 'iterkeys', 'itervalues', 'keys', 'len'

    def subscribeToChanges(self):
        """
        Must only be used inside plugins.

        Subscribes to device changes. This includes state and property changes.

        Every time a device changes, the plugin handler will call the deviceUpdated method.

        :return: None
        """
        ...

    def __iter__(self, filter="") -> List["indigo.Schedule"]: ...


class Schedule:
    #  TODO: Missing methods
    ...

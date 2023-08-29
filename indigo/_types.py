from __future__ import annotations
from typing import Union

import indigo

deviceType = Union[str, int, indigo.Device]
dimmerDeviceType = Union[deviceType, indigo.DimmerDevice]
triggerType = Union[str, int, indigo.Trigger]
variableType = Union[str, int, indigo.Variable]
folderType = Union[str, int, indigo.Folder]

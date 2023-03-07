
import typing as _typing

import indigo.device
import indigo.folder
import indigo.variable
import indigo.trigger
import indigo.server

from ._objects import *
from ._enums import *
from ._plugin import *
from ._utils import *


__version__ = "0.1.0"
__author__ = "Luís Tripa"

devices: _typing.List[Device] = list()
variables: _typing.List[Variable] = list()

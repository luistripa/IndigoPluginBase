from ._types import *
from ._enums import *
from ._folders import *
from ._devices import *
from ._actions import *
from ._triggers import *
from ._variables import *
from ._plugin import *

import indigo.device as device
import indigo.dimmer as dimmer
import indigo.server as server
import indigo.trigger as trigger
import indigo.variable as variable

devices = indigo.DeviceList()
variables = indigo.VariableList()
triggers = indigo.TriggerList()
# TODO: Missing schedules and actionGroups

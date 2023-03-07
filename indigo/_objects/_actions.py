import typing as _typing

from indigo._enums import *
from indigo._utils import Dict


__all__ = [
    'BaseAction',
    'DeviceAction',
    'DisableScheduleAction',
    'DisableTriggerAction',
    'EmailAction',
    'EnableScheduleAction',
    'EnableTriggerAction',
    'ExecuteGroupAction',
    'ExecuteScriptAction',
    'InputOutputAction',
    'ModifyVariableAction',
    'PluginAction',
    'SendInsteonGroupCommandAction',
    'SprinklerAction',
    'ResetInterfacesAction',
    'ThermostatAction',
    'UniversalAction',
]


class BaseAction:
    description: str
    """A description of the action"""

    delayAmount: int
    """Number of seconds to delay before executing the actions (o for none)"""

    replaceExisting: bool
    """If True, then any existing delayed action is replaced by this one."""

    textToSpeak: str
    """This is the text to speak when the action is executed."""

    @property
    def configured(self) -> bool:
        """Returns True if the action is configured, False otherwise."""
        return True

class DeviceAction(BaseAction):
    """API v2.0+ only"""

    complementDelay: int
    """The number of seconds to delay before issuing the complementary action (0 for no action)"""

    deviceId: int
    """The ID of the device to control"""

    deviceAction: kDeviceAction
    """The command to send to the device"""

    actionValue: _typing.Union[int, _typing.Dict]
    """If deviceAction is in [Brighten, Dim, SetBrightness] then this is an integer value."""


class DisableScheduleAction(BaseAction):
    complementDelay: int
    """The number of seconds to delay before issuing the complementary action (0 for no action), in this case an EnableScheduleAction"""

    scheduleId: int
    """The ID of the schedule to disable"""


class DisableTriggerAction(BaseAction):
    complementDelay: int
    """The number of seconds to delay before issuing the complementary action (0 for no action), in this case an EnableTriggerAction"""

    triggerId: int
    """The ID of the trigger to disable"""


class EmailAction(BaseAction):
    emailBody: str
    """The body of the email to send"""

    emailSubject: str
    """The subject of the email to send"""

    emailTo: str
    """The (semicolon separated) list of email addresses"""


class EnableScheduleAction(BaseAction):
    complementDelay: int
    """The number of seconds to delay before issuing the complementary action (0 for no action), in this case a DisableScheduleAction"""

    scheduleId: int
    """The ID of the schedule to enable"""


class EnableTriggerAction(BaseAction):
    complementDelay: int
    """The number of seconds to delay before issuing the complementary action (0 for no action), in this case a DisableTriggerAction"""

    triggerId: int
    """The ID of the trigger to enable"""


class ExecuteGroupAction(BaseAction):
    groupId: int
    """The ID of the action group to execute"""


class ExecuteScriptAction(BaseAction):
    scriptCode: str
    """The code of the script to execute"""


class InputOutputAction(BaseAction):
    deviceId: int
    """The ID of the I/O device to control"""

    action: kIOAction
    """The I/O action to execute"""

    index: int
    """If action is TurnOffOutput, TurnOnOutput, the index of the input or output to control"""


class ModifyVariableAction(BaseAction):
    variableId: int
    """The ID of the variable to modify"""

    variableAction: kVariableAction
    """The action to perform on the variable"""

    variableValue: str
    """The value to set the variable to. Only used if variableAction is SetValue"""


class PluginAction(BaseAction):
    """Action defined by a plugin, and is similar in definition to a CustomPluginDevice"""

    deviceId: int
    """The ID of the plugin device to control"""

    pluginId: str
    """The ID of the plugin to control. Specified in the plugin's Info.plist file"""

    pluginTypeId: str
    """The ID specified in the Actions.xml"""

    props: Dict
    """A dictionary defining this action's properties"""


class SendInsteonGroupCommandAction(BaseAction):
    command: kInstGroupCommand
    """This is the group command to send"""

    group: int
    """This is the group number to send the command to"""


class SprinklerAction(BaseAction):
    """Represents an action to control a sprinkler module"""

    deviceId: int
    """The ID of the sprinkler device to control"""

    multiplierVarId: int
    """API v1.20+ only. Optional elemt ID for tge variable multiplier (None if no multiplier is specified)"""

    sprinklerAction: kSprinklerAction
    """The action to perform on the sprinkler device"""

    zoneDurations: _typing.List[float]
    """List that represent the durations in minutes for each zone to schedule - used when sprinkler action is RunNewSchedule"""

    zoneIndex: int
    """The zone to turn on as a 1-based index - used when sprinklerAction is ZoneOn"""


class ResetInterfacesAction(BaseAction):
    """Thus class represent an action to reset the built-in interfaces
    There are no properties for this action."""
    pass


class ThermostatAction(BaseAction):
    deviceId: int
    """The ID of the thermostat device to control"""

    thermostatAction: kThermostatAction
    """The action to perform on the thermostat device"""

    actionMode: _typing.Union[kFanMode, kHvacMode]
    """If action is SetFanMode, then a kFanMode enumeration.
    If action is setHvacMode, then a kHvacMode enumeration."""

    actionValue: float
    """If action is Decrese* or Increase* the amount to increase/decrese the setpoints.
    If action is Set* the temperature to set the setpoint to"""


class UniversalAction(BaseAction):
    """API v2.0+ only. This class represents a universal action that can be used with devices of different classes.
    Previously this class was named GeneralDeviceAction. It was renamed in API v2.0."""

    deviceId: int
    """The ID of the device to control"""

    deviceAction: kUniversalAction
    """The action to perform on the device"""

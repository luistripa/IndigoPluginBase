import enum


class kStateChange(enum.Enum):
    """Enum that represents the type of state change on a device. Used for triggers. This is used along with the
    kStateSelector enum to determine the type of the trigger."""

    BecomesEqual = 0
    """stateSelector becomesEqual to stateValue.

    Valid for values kStateSelector: ActiveZone AnalogInput BrightnessLevel HumidityInput SensorInput SetpointCool,
    SetpointHeat, TemperatureInput"""

    BecomesFalse = 1
    """stateSelector becomes False.

    Valid for values kStateSelector: BinaryInput, BinaryOutputHvacCoolerIsOn HvacFanIsOn HvacFanModeIsAlwaysOn
    HvacFanModeIsAuto HvacHeaterIsOn HvacOperationModeIsAuto HvacOperationModeIsCool HvacOperationModeIsHeat
    HvacOperationModeIsOff HvacOperationModeIsProgramAuto HvacOperationModeIsProgramCool HvacOperationModeIsProgramHeat
    OnOffState Zone"""

    BecomesGreaterThan = 2
    """stateSelector becomes greater than stateValue.

    Valid for values kStateSelector: AnalogInput BrightnessLevel HumidityInput SensorInput SetpointCool SetpointHeat
    TemperatureInput"""

    BecomesLessThan = 3
    """stateSelector becomes less than stateValue.

    Valid values for kStateSelector: AnalogInput BrightnessLevel HumidityInput SensorInput SetpointCool SetpointHeat
    TemperatureInput"""

    BecomesNotEqual = 4
    """stateSelector becomes not equal to stateValue.

    Valid for values kStateSelector: ActiveZone AnalogInput BrightnessLevel HumidityInput SensorInput SetpointCool
    SetpointHeat TemperatureInput"""

    BecomesTrue = 5
    """stateSelector becomes True.

    Valid for values kStateSelector: BinaryInput BinaryOutput HvacCoolerIsOn HvacFanIsOn HvacFanModeIsAlwaysOn HvacFanModeIsAuto 
    HvacHeaterIsOn HvacOperationModeIsAuto HvacOperationModeIsCool HvacOperationModeIsHeat HvacOperationModeIsOff 
    HvacOperationModeIsProgramAuto HvacOperationModeIsProgramCool HvacOperationModeIsProgramHeat OnOffState Zone"""

    Changes = 6
    """stateSelector changes.

    Valid values for kStateSelector: ActiveZone AnalogInput AnalogInputsAll BinaryInput BinaryInputsAll BinaryOutput 
    BinaryOutputsAll BrightnessLevel HumidityInput HumidityInputsAll HvacCoolerIsOn HvacFanIsOn HvacFanMode 
    HvacFanModeIsAlwaysOn HvacFanModeIsAuto HvacHeaterIsOn HvacOperationModeIsAuto HvacOperationModeIsCool 
    HvacOperationModeIsHeat HvacOperationModeIsOff HvacOperationModeIsProgramAutoHvacOperationModeIsProgramCool
    HvacOperationModeIsProgramHeatOnOffState SensorInput SensorInputsAll SetpointCool SetpointHeat TemperatureInput 
    TemperatureInputsAll Zone"""


class kStateSelector(enum.Enum):
    """Represents the state to be monitored by a trigger. This is used along with the kStateChange enum to determine the
    type of the trigger."""

    ActiveZone = 0
    """Monitor the sprinkler's activeZone to become =, !=, or any change."""

    AnalogInput = 1
    """Monitor (one of) the analog input(s) available on the device for =, !=, <, >, or any change.
    stateSelectorIndex is required to be in the range of available inputs."""

    AnalogInputsAll = 2
    """Monitors all of the analog inputs available on the device for any change."""

    BinaryInput = 3
    """Monitor (one of) the binary input(s) to become true, false, or any change.
    stateSelectorIndex is required to be in the range of available inputs."""

    BinaryInputsAll = 4
    """Monitors all of the binary inputs available on the device for any change"""

    BinaryOutput = 5
    """Monitor (one of) the binary output(s) to become true, false, or any change,
    stateSelectorIndex is required to be in the range of available outputs."""

    BinaryOutputsAll = 6
    """Monitors all of the binary outputs available on the device for any change"""

    BrightnessLevel = 7
    """monitor the brightness level of a device for =, !=, <, >, and any change."""

    HumidityInput = 8
    """Monitor (one of) the humdity sensor(s) available on the device for =, !=, <, >, and any change.
    stateSelectorIndex is required to be in the range of available inputs."""

    HumidityInputsAll = 9
    """Monitors all of the humidity sensors available on the device for any change."""

    HvacCoolerIsOn = 10
    """Monitor the thermostat for any time the air conditioning turns on, off, or has any change
    (coolIsOn is the current compressor state)"""

    HvacFanIsOn = 11
    """Monitor the thermostat for any time the fan turns on, off, or has any change
    (fanIsOn is the current fan state)"""

    HvacFanMode = 12
    """Monitor the fanMode of the thermostat for any change"""

    HvacFanModeIsAlwaysOn = 13
    """Monitor the fanMode of the thermostat for a change to/from kFanMode.AlwaysOn"""

    HvacFanModeIsAuto = 14
    """Monitor the fanMode of the thermostat for a change to/from kFanMode.AutoOn"""

    HvacHeaterIsOn = 15
    """Monitor the thermostat for any time the heater turns on, off, or has any change
    (heatIsOn is the current heater state)"""

    HvacOperationMode = 16
    """Monitor the hvacMode of the thermostat for any change"""

    HvacOperationModeIsAuto = 17
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.HeatCoolOn"""

    HvacOperationModeIsCool = 18
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.CoolOn"""

    HvacOperationModeIsHeat = 19
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.HeatOn"""

    HvacOperationModeIsOff = 20
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.Off"""

    HvacOperationModeIsProgramAuto = 21
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.ProgramAuto"""

    HvacOperationModeIsProgramCool = 22
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.ProgramCool"""

    HvacOperationModeIsProgramHeat = 23
    """Monitor the hvacMode of the thermostat for a change to/from kHvacMode.ProgramHeat"""

    KeypadButtonLed = 24
    """There is no documentation for this enum value"""  # FIXME: No documentation

    OnOffState = 25
    """Monitor the device for a change to/from on/off"""

    SensorInput = 26
    """Monitor (one of) the sensor input(s) available on the device for =, !=, <, >, or any change.
    stateSelectorIndex is required to be in the range of available inputs."""

    SensorInputsAll = 27
    """Monitors all of the sensor inputs available on the device for any change"""

    SetpointCool = 28
    """Monitor the cool setpoint of the thermostat for =, !=, <, >, or any change"""

    SetpointHeat = 29
    """Monitor the heat setpoint of the thermostat for =, !=, <, >, or any change"""

    TemperatureInput = 30
    """Monitor (one of) the temperature sensor(s) available on the device for =, !=, <, >, and any change.
    stateSelectorIndex is required to be in the range of available inputs."""

    TemperatureInputsAll = 31
    """Monitors all of the temperature sensors available on the device for any change."""

    Zone = 32
    """Monitor (one of) the binary output(s) to become true, false, or any change.
    stateSelectorIndex is required to be in the range of available outputs."""


class kEmailFilter(enum.Enum):
    AnyEmail = 0
    """When any email is received."""

    MatchEmailFields = 1
    """When email subject/from fields match."""
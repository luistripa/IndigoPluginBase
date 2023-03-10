
import enum


class kDeviceAction(enum.Enum):
    AllLightsOff = 1
    AllLightsOn = 2
    AllOff = 3
    BrightenBy = 4
    DimBy = 5
    Lock = 6
    Unlock = 7
    SetBrightness = 6
    SetColorLevels = 7
    Toggle = 8
    TurnOff = 9
    TurnOn = 10
    Open = 11
    Close = 12
    RequestStatus = 13


class kIOAction(enum.Enum):
    TurnOffOutput = 1  # Turn off output specified by index
    TurnOffAllOutputs = 2  # Turn off all outputs
    TurnOnOutput = 3  # Turn on output specified by index
    RequestStatusAll = 4  # Request status of all inputs and outputs
    RequestAnalogInputValues = 5
    RequestBinaryInputsStatus = 6
    RequestBinaryOutputsStatus = 7
    RequestSensorInputValues = 8


class kVariableAction(enum.Enum):
    DecrementValue = 1
    IncrementValue = 2
    SetValue = 3  # Set the value to the variableValue property


class kInstGroupCommand(enum.Enum):
    Value = 1  # Description
    InstantOff = 2  # Send the instant (fast) off command to group ignoring ramp rate
    InstantOn = 3  # Send the instant (fast) on command to group ignoring ramp rate
    Off = 4  # Send the off command to group
    On = 5  # Send the on command to group


class kSprinklerAction(enum.Enum):
    RunNewSchedule = 1  # Run a new schedule
    RunPreviousSchedule = 2  # Run the previous schedule
    PauseSchedule = 3  # Pause the current schedule
    ResumeSchedule = 4  # Resume the current schedule
    StopSchedule = 5  # Stop the current schedule
    NextZone = 6  # Run the next zone in the current schedule
    ZoneOn = 7  # Turn on the specified zone
    AllZonesOff = 8  # Turn off all zones
    RequestStatusAll = 9  # Request status of all zones


class kThermostatAction(enum.Enum):
    DecreaseCoolSetpoint = 1
    DecreaseHeatSetpoint = 2
    IncreaseCoolSetpoint = 3
    IncreaseHeatSetpoint = 4
    SetCoolSetpoint = 5
    SetFanMode = 6
    SetHeatSetpoint = 7
    SetHvacMode = 8
    RequestStatusAll = 9
    RequestMode = 10
    RequestEquipmentState = 11
    RequestTemperatures = 12
    RequestHumidities = 13
    RequestDeadbands = 14
    RequestSetpoints = 15


class kFanMode(enum.Enum):
    AlwaysOn = 1
    Auto = 2


class kHvacMode(enum.Enum):
    Cool = 1
    HeatCool = 2
    Heat = 3
    Off = 4
    ProgramHeatCool = 5
    ProgramCool = 6
    ProgramHeat = 7


class kUniversalAction(enum.Enum):
    Beep = 1
    EnergyUpdate = 2
    EnergyReset = 3
    RequestStatus = 4

import enum


class kProtocol(enum.Enum):
    Insteon = 1
    X10 = 2
    ZWave = 3
    Plugin = 4


class kAllDeviceSel(enum.Enum):
    Insteon = 1
    X10 = 2
    ZWave = 3


class kStateImageSel(enum.Enum):
    Auto = 1
    NoImage = 2
    Error = 3
    Custom = 4
    PowerOff = 5
    PowerOn = 6
    DimmerOff = 7
    DimmerOn = 8
    FanOff = 9
    FanLow = 10
    FanMedium = 11
    FanHigh = 12
    SprinklerOff = 13
    SprinklerOn = 14
    HvacOff = 15
    HvacCoolMode = 16
    HvacHeatMode = 17
    HvacAutoMode = 18
    HvacFanOn = 19
    HvacCooling = 20
    HvacHeating = 21
    SensorOff = 22
    SensorOn = 23
    SensorTripped = 24
    EnergyMeterOff = 25
    EnergyMeterOn = 26
    LightSensor = 27
    LightSensorOn = 28
    MotionSensor = 29
    MotionSensorTripped = 30
    DoorSensorClosed = 31
    DoorSensorOpen = 32
    WindowSensorClosed = 33
    WindowSensorOpen = 34
    TemperatureSensor = 35
    TemperatureSensorOn = 36
    HumiditySensor = 37
    HumiditySensorOn = 38
    Humidifier = 39
    HumidifierOn = 40
    Dehumidifier = 41
    DehumidifierOn = 42
    TimerOff = 43
    TimerOn = 44
    AvStopped = 45
    AvPaused = 46
    AvPlaying = 47
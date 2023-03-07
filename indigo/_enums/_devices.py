import enum as _enum


__all__ = [
    'kProtocol',
    'kAllDeviceSel',
    'kStateImageSel',
]


class kProtocol(_enum.Enum):
    Insteon = 1
    X10 = 2
    ZWave = 3
    Plugin = 4


class kAllDeviceSel(_enum.Enum):
    Insteon = 1
    X10 = 2
    ZWave = 3


# Must be done this way because of "None" value, which is a python reserved keyword.
kStateImageSel = _enum.Enum("kStateImageSel", [
    "Auto", "None", "Error", "Custom", "PowerOff", "PowerOn", "DimmerOff", "DimmerOn", "FanOff",
    "FanLow", "FanMedium", "Fan High", "SprinklerOff", "SprinklerOn", "HvacOff", "HvacCoolMode",
    "HvacHeatMode", "HvacAutoMode", "HvacFanOn", "HvacCooling", "HvacHeating", "SensorOff",
    "SensorOn", "SensorTripped", "EnergyMeterOff", "EnergyMeterOn", "LightSensor", "LightSensorOn",
    "MotionSensor", "MotionSensorTripped", "DoorSensorClosed", "DoorSensorOpen", "WindowSensorClosed",
    "WindowSensorOpen", "TemperatureSensor", "TemperatureSensorOn", "HumiditySensor", "HumiditySensorOn",
    "Humidifier", "HumidifierOn", "Dehumidifier", "DehumidifierOn", "TimerOff", "TimerOn", "AvStopped",
    "AvPaused", "AvPlaying"
])

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import _types


def isEnabled() -> bool:
    """Returns True if the Z-Wave interface is enabled, False otherwise."""
    ...


def sendRaw(device: _types.deviceType, nodeId: int, endpoint: int,
            cmdBytes: bytes, sendMode: int, waitUntilAck=True):
    """Send a raw zwave command to a device.
    :param device: optional - The device to send the command to. If not specified, must specify nodeId
    :param nodeId: optional - The node id of the device to send the command to. If not specified, must specify device
    :param endpoint: optional - The endpoint of the device to send the command to. If a nodeId is specified and supports multiple endpoints
    :param cmdBytes: The raw bytes to send
    :param sendMode: The send mode to use. 0: immediate, 1: immediate first, if no ACK wait for wake, 2: wait for wake
    :param waitUntilAck: optional - Waits for an ACK from the device before returning. Default is True."""
    ...


def sendConfiParam(device: _types.deviceType, nodeId: int, endpoint: int,
                   paramIndex: int, paramSize: int, paramValue: int, waitUntilAck=True):
    """Modify a Z-Wave configuration parameter.
    :param device: optional - The device to send the command to. If not specified, must specify nodeId
    :param nodeId: optional - The node id of the device to send the command to. If not specified, must specify device
    :param endpoint: optional - The endpoint of the device to send the command to. If a nodeId is specified and supports multiple endpoints
    :param paramIndex: The index of the parameter to modify
    :param paramSize: The size of the parameter to modify
    :param paramValue: The new value of the parameter
    :param waitUntilAck: optional - Waits for an ACK from the device before returning. Default is True."""
    ...


def startNetworkOptimize(nodeId: int):
    """Starts the network optimization process for a node or all nodes.
    :param nodeId: optional - The node id of the node to optimize. If not specified optimized the entire network."""
    ...


def stopNetworkOptimize():
    """Stops the network optimization process."""
    ...


def enterInclusionMode(useEncryption: bool):
    """Puts the Z-Wave interface into inclusion mode.
    :param useEncryption: There is no API documentation for this parameter."""


def enterExclusionMode():
    """Puts the Z-Wave interface into exclusion mode."""
    ...


def exitInclusionExclusionMode():
    """Exits inclusion or exclusion mode."""
    ...


def subscribeToIncoming():
    """Subscribes to all incoming Z-Wave commands."""
    ...


def subscribeToOutgoing():
    """Subscribes to all outgoing Z-Wave commands."""
    ...
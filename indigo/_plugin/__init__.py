import webbrowser

from deprecation import deprecated

import indigo
import logging


class PluginInfo:

    pluginId: str = "IndigoPluginBase"
    pluginVersion: str = "1.0.0"
    pluginSupportURL: str = ""

    def isInstalled(self) -> bool:
        return True

    def isEnabled(self) -> bool:
        return True

    def isRunning(self) -> bool:
        return True

    def restart(self, waitUnitlDone=True):
        pass

    def executeAction(self, actionId: str, deviceId: int, props: dict):
        pass

    # TODO: Add more methods


class PluginBase:
    class StopThread(Exception):
        pass

    def __init__(self, pluginId: str, pluginDisplayName: str, pluginVersion: str, pluginPrefs: dict):
        """
        Constructor for the PluginBase class.

        To do any initializations, override the startup() method instead.

        :param pluginId: The plugin's unique identifier.
        :param pluginDisplayName: The plugin's display name.
        :param pluginVersion: The plugin's version.
        :param pluginPrefs: The plugin's preferences. As defined in the plugin's configuration.
        """
        self.pluginId = pluginId
        self.pluginDisplayName = pluginDisplayName
        self.pluginVersion = pluginVersion
        self.pluginPrefs = pluginPrefs
        self.stopThread = False

        self.logger = logging.getLogger(pluginId)
        self.debug = False

    def __del__(self) -> None:
        """
        Destructor for the PluginBase class.

        :return:
        """
        pass

    def startup(self) -> None:
        """
        Do any initializations here.

        :return: None
        """
        self.__del__()

        pass

    def shutdown(self) -> None:
        """
        Do any cleanups here.

        :return: None
        """
        pass

    def runConcurrentThread(self):
        """
        This method is called when the plugin is started. Indigo automatically calls this method.

        Example of a basic implementation:
        <code>
        def runConcurrentThread(self):
            try:
                while True:
                    self.sleep(1)
            except self.StopThread:
                pass
        </code>

        :return: None
        """
        raise NotImplementedError

    def stopConcurrentThread(self):
        """
        This method will get called when the IndigoServer wants your plugin to stop any threads that it may have created.

        The default behavior only changes the stopThread flag to True, which causes the self.sleep() method to throw
        a StopThread exception that you have to handle in the runConcurrentThread() method.

        :return: None
        """
        self.stopThread = True

    def closedPrefsConfigUi(self, valuesDict: dict, userCancelled: bool) -> None:
        """
        This method is called when the user closes the plugin's preferences dialog.

        :param valuesDict: The values of the preferences' dialog.
        :param userCancelled: True if the user cancelled the dialog, False otherwise.
        :return: None
        """
        pass

    def prepareToSleep(self) -> None:
        """
        The defaul implementation will call the deviceStopComm() method for all devices and triggerStopProcessing() for
        all triggers. Can be overridden to do other things.
        :return:
        """
        pass

    def wakeUp(self) -> None:
        """
        The default implementation will call the deviceStartComm() method for all devices and triggerStartProcessing() for
        all triggers. Can be overridden to do other things.
        :return:
        """
        pass

    def getDeviceStateList(self, dev: indigo.Device) -> indigo.List:
        """
        If your plugin defines custom devices, this method will be called by the server when it tries to build the state list for your device.

        The default implementation just returns the <States> element (reformatted as an indigo.List()
        that's available to your plugin via devicesTypeDict[“yourCustomTypeIdHere”]) in your Devices.xml file.

        You can, however, implement the method yourself to return a custom set of states.
        For instance, you may want to allow the user to create custom labels for the various inputs on your device
        rather than use generic “Input 1”, “Input 2”, etc., labels. Check out the EasyDAQ plugin for an example.
        :param dev: The device to get the state list for.
        :return: The state list for the device.
        """
        pass

    def getDeviceDisplayStateId(self, dev: indigo.Device) -> None:
        """
        If your plugin defines custom devices, this method will be called by the server to determine which
        device state ID to display in the device list UI state column.

        The default implementation just returns the <UiDisplayStateId> element in your Devices.xml file.
        You can, however, implement the method the plugin needs to dynamically determine the which state ID to display.

        :param dev: The device to get the display state ID for.
        :return: The state ID to display.
        """
        pass

    def deviceStartComm(self, dev: indigo.Device) -> None:
        """
        This method is called when a device is starting up. Any work related to the device initialization should be done here.

        :param dev: The device that is starting up.
        :return: None
        """
        pass

    def deviceStopComm(self, dev: indigo.Device) -> None:
        """
        This method is called when a device is shutting down. Any work related to the device shutdown should be done here.

        :param dev: The device that is shutting down.
        :return: None
        """
        pass

    def didDeviceCommPropertyChange(self, origDev: indigo.Device, newDev: indigo.Device) -> bool:
        """
        This method gets called by the default implementation of deviceUpdated() to determine if any of the
        properties needed for device communication (or any other change requires a device to be stopped and restarted).

        The default implementation checks for any changes to properties. You can implement your own to provide more granular results

        For instance, if your device requires 4 parameters, but only 2 of those parameters requires that you restart the device,
        then you can check to see if either of those changed. If they didn't then you can just return False and
        your device won't be restarted (via deviceStopComm()/deviceStartComm() calls).

        :param origDev: The original device.
        :param newDev: The new device.
        :return: True if device should be restarted, False otherwise.
        """
        return False

    def deviceUpdated(self, origDev: indigo.Device, newDev: indigo.Device) -> None:
        """
        Complementary to the deviceCreated() method described above, but signals device updates.
        You'll get a copy of the old device object as well as the new device object.

        The default implementation of this method will do a few things for you:
        if either the old or new device are devices defined by you, and if the device type changed OR
        the communication-related properties have changed (as defined by the didDeviceCommPropertyChange() method - see above for details)
        then deviceStopComm() and deviceStartComm() methods will be called as necessary
        (stop only if the device changed to a type that isn't your device, start only if the device changed to a type
        that belongs to you, or both if the props/type changed and they both belong to you).

        :param origDev: The original device.
        :param newDev: The new device.
        :return: None
        """

        if origDev.pluginId == self.pluginId and newDev.pluginId == self.pluginId:
            if origDev.deviceTypeId != newDev.deviceTypeId:
                self.deviceStopComm(origDev)
                self.deviceStartComm(newDev)

            elif self.didDeviceCommPropertyChange(origDev, newDev):
                self.deviceStopComm(origDev)
                self.deviceStartComm(newDev)

        else:  # One of the devices is not ours (user changed plugin for device)
            if origDev.pluginId == self.pluginId:
                self.deviceStopComm(origDev)
            if newDev.pluginId == self.pluginId:
                self.deviceStartComm(newDev)

    def deviceDeleted(self, dev: indigo.Device) -> None:
        """
        Complementary to the deviceCreated() method described above, but signals device deletes.

        The default implementation just checks to see if the device belongs to your plugin and if so calls the deviceStopComm() method.
        If you implement this method you'll need to call deviceStopComm() yourself or duplicate the functionality here.

        :param dev: The device that is being deleted.
        :return: None
        """
        if dev.pluginId == self.pluginId:
            self.deviceStopComm(dev)

    def triggerStartProcessing(self, trigger: indigo.Trigger) -> None:
        """
        If your plugin defines events, this is likely the place where you'll want to do the work to start watching for those events to occur.
        For instance, let's say that you have an event for a plugin update, then you'll want to periodically check your site to see if there's a new version available.
        This is where you'd start that process.

        When conditions are met in your plugin for a trigger to be executed, you would call indigo.trigger.execute(triggerReference)
        to tell the Server to execute the trigger (and it's conditions).

        :param trigger: The trigger that is starting up.
        :return: None
        """
        pass

    def triggerStopProcessing(self, trigger: indigo.Trigger) -> None:
        """
        This is the complementary method to triggerStartProcessing() - it gets called when the event should no longer be active/enabled.
        For instance, when the user disables or deletes a trigger, this method gets called.

        :param trigger: The trigger that is shutting down.
        :return: None
        """
        pass

    def didTriggerProcessingPropertyChange(self, origTrigger: indigo.Trigger, newTrigger: indigo.Trigger) -> bool:
        """
        Much like its device counterpart above (didDeviceCommPropertyChange()), this method gets called by the default implementation of triggerUpdated()
        to determine if any of the properties needed for recognizing an event have changed.

        The default implementation checks for any changes to any properties.

        :param origTrigger: The original trigger.
        :param newTrigger: The new trigger.
        :return: True if trigger should be restarted, False otherwise.
        """
        return False

    def triggerCreated(self, trigger: indigo.Trigger) -> None:
        """
        This method will get called whenever a new trigger defined by your plugin is created.

        In many circumstances, you won't need to implement this method since the default behavior
        (which is to call the triggerStartProcessing() method if it's your trigger and it's enabled) is what you want anyway
        (see the triggerStartProcessing() method above for details).
        However, if for some reason you need to know when a trigger is created, but before your plugin is asked to start watching for the appropriate conditions,
        this method can provide that hook. If you implement this method, you'll need to either call triggerStartProcessing() or duplicate the functionality here.

        You can also have this method called for triggers that don't belong to your plugin.
        If, for instance, you want to know when all triggers are created (and updated/deleted),
        you can call the indigo.triggers.subscribeToChanges() method to have the IndigoServer send all trigger creation/update/deletion notifications.
        As with other change subscriptions, this should be used very sparingly since it's a lot of overhead both for your plugin and, more importantly, for the IndigoServer.

        :param trigger: The trigger that is being created.
        :return: None
        """
        if trigger.pluginId == self.pluginId:
            self.triggerStartProcessing(trigger)

    def triggerUpdated(self, origTrigger: indigo.Trigger, newTrigger: indigo.Trigger) -> None:
        """
        Complementary to the triggerCreated() method described above, but signals trigger updates.
        You'll get a copy of the old trigger object as well as the new trigger object.

        The default implementation of this method will do a few things for you:
        if either the old or new trigger are triggers defined by you, and if the trigger type changed OR
        the communication-related properties have changed (as defined by the didTriggerProcessingPropertyChange() method - see above for details)
        then triggerStopProcessing() and triggerStartProcessing() methods will be called as necessary.

        :param origTrigger:
        :param newTrigger:
        :return:
        """
        if origTrigger.pluginId == self.pluginId and newTrigger.pluginId == self.pluginId:
            if origTrigger.deviceTypeId != newTrigger.deviceTypeId:
                self.triggerStopProcessing(origTrigger)
                self.triggerStartProcessing(newTrigger)

            elif self.didDeviceCommPropertyChange(origTrigger, newTrigger):
                self.triggerStopProcessing(origTrigger)
                self.triggerStartProcessing(newTrigger)

        else:  # One of the triggers is not ours (user changed plugin for trigger)
            if origTrigger.pluginId == self.pluginId:
                self.triggerStopProcessing(origTrigger)
            if newTrigger.pluginId == self.pluginId:
                self.triggerStartProcessing(newTrigger)

    def triggerDeleted(self, trigger: indigo.Trigger) -> None:
        """
        Complementary to the triggerCreated() method described above, but signals trigger deletes.

        The default implementation just checks to see if the trigger belongs to your plugin and if so calls the triggerStopProcessing() method.
        If you implement this method you'll need to call triggerStopProcessing() yourself or duplicate the functionality here.

        :param trigger: The trigger that is being deleted.
        :return: None
        """
        if trigger.pluginId == self.pluginId:
            self.triggerStopProcessing(trigger)

    def variableCreated(self, var: indigo.Variable) -> None:
        """
        This method will get called whenever a new variable is created.
        You can call the indigo.variables.subscribeToChanges() method to have the IndigoServer send all variable creation/update/deletion notifications.
        As with other change subscriptions, this should be used very sparingly since it's a lot of overhead both for your plugin and, more importantly, for the IndigoServer.

        :param var: The variable that is being created.
        :return: None
        """
        pass

    def variableUpdated(self, origVar: indigo.Variable, newVar: indigo.Variable) -> None:
        """
        Complementary to the variableCreated() method described above, but signals variable updates.
        You'll get a copy of the old variable object as well as the new variable object.

        :param origVar: The original variable.
        :param newVar: The new variable.
        :return: None
        """
        pass

    def variableDeleted(self, var: indigo.Variable) -> None:
        """
        Complementary to the variableCreated() method described above, but signals variable deletes.

        :param var: The variable that is being deleted.
        :return: None
        """
        pass


    def actionControlDevice(self, action: indigo.DeviceAction):
        """
        This method is called when the user clicks on the turn on/off ou status request buttons in the Indigo UI.

        :param action: The action to perform on the device.
        :return:
        """
        pass

    """
    HELPER METHODS
    """

    def applicationWithBundleIdentifier(self, bundleID: str):
        """
        TODO: Find documentation for this method.
        :param bundleID: ?
        :return: ?
        """
        pass

    def browserOpen(self, url) -> None:
        """
        This method will open the specified in the default browser.
        Note it does so on the server machine and not on any remotely connected clients.

        :param url: The URL to open.
        :return: None
        """
        webbrowser.open(url)

    @deprecated("Use self.logger instead.")
    def debugLog(self, msg: str) -> None:
        """
        If, at any point in your plugin, you set self.debug = True, then any time debugLog is called the string will get inserted into Indigo's event log.
        If self.debug = False (the default) any call to debugLog does nothing.

        :param msg: The message to log.
        :return: None
        """
        if self.debug:
            self.logger.debug(msg)

    @deprecated("Use self.logger instead.")
    def errorLog(self, msg: str) -> None:
        """
        This method will insert the specified string into Indigo's event log.

        :param msg: The message to log.
        :return: None
        """
        if self.debug:
            self.logger.error(msg)

    def openSerial(self, ownerName: str, portUrl: str, baudrate: int, bytesize: int, parity, stopbits, timeout, xonxoff, rtscts, writeTimeout, dsrdtr, interCharTimeout):
        """
        This method is identical to creating a new pySerial Serial object except that it never throws an exception.
        If the serial connection cannot be opened then None is returned and an error will be automatically logged to the Indigo Server event log.

        :param ownerName: The name of the device or plugin that owns this serial port (used for logging purposes). Make sure it's ASCII text with no unicode characters.
        :param: All other arguments passed directly to the pySerial Serial object constructor.
        :return:
        """
        pass

    def sleep(self, seconds):
        """
        This method should be called from within your plugin's runConcurrentThread() defined method, if it is defined.
        It will automatically raise the StopThread exception when the Indigo Server is trying to shut down or restart the plugin.
        See runConcurrentThread documentation above for more details.

        :param seconds: The number of seconds to sleep.
        :return: None
        """
        pass

    
    def zwaveCommandReceived(self, cmd: dict):
        """Method called when a Z-Wave command is received by Indigo. Requires indigo.zwave.subscribeToIncoming() to be called.
        :param cmd: A dictionary containing the following keys: bytes, nodeId, endpoint"""
        ...

    def zwaveCommandSent(self, cmd: dict):
        """Method called when a Z-Wave command is sent by Indigo. Requires indigo.zwave.subscribeToOutgoing() to be called.
        :param cmd: A dictionary containing the following keys: bytes, timeDelta, cmdSuccess, nodeId, endpoint"""
        ...
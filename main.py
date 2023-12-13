import indigo
import indigo._types


class Plugin(indigo.PluginBase):
    def zwaveCommandReceived(self, cmd):
        return super().zwaveCommandReceived(cmd)
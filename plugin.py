import indigo


class Plugin(indigo.PluginBase):
    def runConcurrentThread(self):
        while True:
            self.sleep(1)

    def deviceStartComm(self, dev) -> None:
        super().deviceStartComm(dev)

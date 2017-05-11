from threading import Thread


class PyroDaemonThread(Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        self._daemon = daemon

    def worker(self):
        self._daemon.requestLoop()

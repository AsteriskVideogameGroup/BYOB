from threading import Thread

import Pyro4

from src.utility.metaclasses.MetaSingleton import MetaSingleton
from src.utility.netmiddleware.INetMiddlewareAdapter import INetMiddlewareAdapter
# from src.utility.netmiddleware.pyro.PyroDaemonThread import PyroDaemonThread

class PyroNetMiddlewareAdapter(INetMiddlewareAdapter, metaclass=MetaSingleton):
    def __init__(self):
        self._pyrodaemon = Pyro4.Daemon()
        self._nameserver = Pyro4.locateNS()

    def register(self, obj: object, name: str):
        uri = self._pyrodaemon.register(obj)
        self._nameserver.register(name, uri)

    def unregister(self, obj: object = None, name: str = "none"):
        pass

    def setPeerResolverURI(self, uri: str):
        pass

    def getProxy(self, name: str) -> object:
        pass


    def initService(self):

        def serverWorker(daemon):
            daemon.requestLoop()

        threadserver = Thread(target=serverWorker, args=(self._pyrodaemon,))
        threadserver.start()

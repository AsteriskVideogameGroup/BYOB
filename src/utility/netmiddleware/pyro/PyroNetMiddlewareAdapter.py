from threading import Thread

import Pyro4

from src.utility.metaclasses.MetaSingleton import MetaSingleton
from src.utility.netmiddleware.INetMiddlewareAdapter import INetMiddlewareAdapter


class PyroNetMiddlewareAdapter(INetMiddlewareAdapter, metaclass=MetaSingleton):
    def __init__(self):
        self._pyrodaemon = Pyro4.Daemon()
        self._nameserver = None

    def register(self, obj: object, name: str):
        uri = self._pyrodaemon.register(obj)
        # print(Pyro4.config.SERIALIZERS_ACCEPTED)
        self._nameserver.register(name, uri)

    def unregister(self, obj: object = None, name: str = "none"):
        pass

    def setNameServerAddress(self, host: str, port: int):
        self._nameserver = Pyro4.locateNS(host, port)

    def getProxy(self, name: str):
        uri = self._nameserver.lookup(name)
        return Pyro4.Proxy(uri)

    def initService(self):
        Pyro4.config.SERIALIZER = "pickle"

        def serverWorker(daemon):
            print(Pyro4.config.SERIALIZER)
            daemon.requestLoop()

        threadserver = Thread(target=serverWorker, args=(self._pyrodaemon,))
        threadserver.start()

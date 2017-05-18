from src.utility.metaclasses.MetaSingleton import MetaSingleton
from src.utility.settings.GlobalSettings import GlobalSettings
from src.utility.netmiddleware.INetMiddlewareAdapter import INetMiddlewareAdapter

# adapter possibili
from src.utility.netmiddleware.pyro.PyroNetMiddlewareAdapter import PyroNetMiddlewareAdapter


class NetworkObjectTranslator(metaclass=MetaSingleton):
    _NETMIDDLEWARETRASNSLATOR = "netmiddlewaretrasnslator"

    def __init__(self):
        self._middlewareadapter: INetMiddlewareAdapter = None

    def init(self, host: str, port: int):
        """
        Initalize the factory
        """

        # associazione con l'adapter del middleware
        middlewareadapterclass = GlobalSettings().getSetting(NetworkObjectTranslator._NETMIDDLEWARETRASNSLATOR)
        self._middlewareadapter = eval(middlewareadapterclass)()

        # inizializzazione dell'adapter
        self._middlewareadapter.setNameServerAddress(host, port)
        self._middlewareadapter.initService()

    def translate(self, proxyname: str):
        return self._middlewareadapter.getProxy(proxyname)

    def register(self, local_object: object, name: str):
        self._middlewareadapter.register(local_object, name)

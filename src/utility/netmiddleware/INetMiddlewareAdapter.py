import abc

from src.utility.metaclasses.MetaSingleton import MetaAbstractSingleton


class INetMiddlewareAdapter(metaclass=MetaAbstractSingleton):
    @abc.abstractmethod
    def initService(self):
        """
        Init of the middleware service
        """
        pass

    @abc.abstractmethod
    def register(self, obj: object, name: str):
        """
        Register an object in the naming system
        :param obj: object to register
        :param name: name of the object in the resolver
        """
        pass

    @abc.abstractmethod
    def unregister(self, obj: object = None, name: str = "none"):
        """
        Unregister an object in the naming system
        :param obj: object to unregister
        :param name: name of the object in the resolver
        """
        pass

    @abc.abstractmethod
    def getProxy(self, name: str) -> object:
        """
        Get a specified proxy from the system
        :param name: name of the proxy
        """
        pass

    @abc.abstractmethod
    def setNameServerAddress(self, host: str, port: int):
        pass


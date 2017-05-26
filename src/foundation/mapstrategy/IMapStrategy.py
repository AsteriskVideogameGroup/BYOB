import abc

from src.foundation.metaclasses.MetaSingleton import MetaAbstractSingleton


class IMapStrategy(metaclass=MetaAbstractSingleton):

    @abc.abstractmethod
    def disposeDestrObstacles(self, dstrobstacles: list, dim, bobs: list) -> list:
        pass

    @abc.abstractmethod
    def disposeUndestrObstacles(self, undstrobstacles: list, dim) -> list:
        pass

    @abc.abstractmethod
    def disposeBoBs(self, bobs: list, dim):
        pass

    @abc.abstractmethod
    def disposePowerUps(self, powerups: list, dim, occpositions: dict) -> list:
        pass
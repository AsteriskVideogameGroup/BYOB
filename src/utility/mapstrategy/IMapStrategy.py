import abc

from src.utility.geometrictools import Dimensions
from src.utility.metaclasses import MetaAbstractSingleton


class IMapStrategy(metaclass=MetaAbstractSingleton):

    @abc.abstractmethod
    def disposeDestrObstacles(self, dstrobstacles: list, dim: Dimensions, bobs: list) -> list:
        pass

    @abc.abstractmethod
    def disposeUndestrObstacles(self, undstrobstacles: list, dim: Dimensions) -> list:
        pass

    @abc.abstractmethod
    def disposeBoBs(self, bobs: list, dim: Dimensions):
        pass

    @abc.abstractmethod
    def disposePowerUps(self, powerups: list, dim: Dimensions) -> list:
        pass
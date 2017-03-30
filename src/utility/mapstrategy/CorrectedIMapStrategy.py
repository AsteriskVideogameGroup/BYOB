import abc
from src.utility import Dimensions


class IMapStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def disposeDestrObstacles(self, dstrobstacles: list, mapdimensions: Dimensions):
        pass

    @abc.abstractmethod
    def disposeUndestrObstacles(self, undstrobstacles: list, dim: Dimensions) -> list:
        pass

    @abc.abstractmethod
    def disposeBoBs(self, bobs: list, dim: Dimensions) -> list:
        pass

    @abc.abstractmethod
    def disposePowerUps(self, powerups: list, mapdimensions: Dimensions):
        pass

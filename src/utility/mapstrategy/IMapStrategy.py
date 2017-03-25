import abc
from src.model.domain.Map import Map


class IMapStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def disposeDestrObstacles(self, map: Map, dstrobstacles: list):
        pass

    @abc.abstractmethod
    def disposeUndestrObstacles(self, map: Map, undstrobstacles: list):
        pass

    @abc.abstractmethod
    def disposeBoBs(self, map: Map, bobs: list):
        pass

    @abc.abstractmethod
    def disposePowerUps(self, map: Map, powerups: list):
        pass

import abc
from src.model.domain import IMapElement


class IObstacle(IMapElement, metaclass=abc.ABCMeta):
    pass

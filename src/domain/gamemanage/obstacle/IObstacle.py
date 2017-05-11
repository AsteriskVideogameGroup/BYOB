import abc

from src.domain.gamemanage.gameessentials.IMapElement import IMapElement


class IObstacle(IMapElement, metaclass=abc.ABCMeta):
    pass

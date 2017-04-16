import abc
from src.domain.gamemanage.gameessentials.IMapElement import IMapElement


class IPowerUp(IMapElement, metaclass=abc.ABCMeta):
    pass


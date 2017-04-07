import abc
from src.model.domain import IMapElement


class IPowerUp(IMapElement, metaclass=abc.ABCMeta):
    pass

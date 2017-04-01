import abc
from src.utility import Position


class IMapElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setPosition(self, position: Position):
        """
        Set the position for the element
        :param position: position to set
        """

        pass

    @abc.abstractmethod
    def getPosition(self) -> Position:
        """
        Getter of the position of the element
        :return: element's position
        """

        pass

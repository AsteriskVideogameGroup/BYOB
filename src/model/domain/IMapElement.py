import abc
from src.utility.Position import *

class IMapElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setPosition(self, position: Position):
        """
        Set the position for the element
        :param position: position to set
        """

        pass

    @abc.abstractmethod
    def getPosition(self):
        """
        Getter of the position of the element
        :return: element's position
        """

        pass
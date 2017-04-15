import abc

import src.utility.geometrictools as geometrictools


class IMapElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setPosition(self, position: geometrictools.Position):
        """
        Set the position for the element
        :param position: position to set
        """

        pass

    @abc.abstractmethod
    def getPosition(self) -> geometrictools.Position:
        """
        Getter of the position of the element
        :return: element's position
        """

        pass
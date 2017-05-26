import abc


class GIMapElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setPosition(self, position):
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

    def setSprites(self, sprites: dict):
        """
        Set the sprites for the element
        :param sprites: Sprites for each state
        """
        pass

    def getSpriteByState(self, state: str):
        """
        Get the sprite suitable for the state
        :param state: current state
        """
        pass

import abc
from src.model.domain.obstacle.DestructibleObstacle import *
from src.model.domain.obstacle.UndestructibleObstacle import *
from src.model.domain.powerup.IPowerUp import *


class IEnvironmentObjectFactory(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def getInstance(cls):
        pass

    @abc.abstractmethod
    def getDestructibleObstacles(self) -> list:
        """
        Getter for the destructible obstacles for a given mode

        :return: a list of differents destructible obstacles
        """
        pass

    @abc.abstractmethod
    def getUndestructibleOstacles(self) -> list:
        """
        Getter for the destructible obstacles for a given mode

        :return: a list of differents destructible obstacles
        """
        pass

    @abc.abstractmethod
    def getPowerUps(self) -> list:
        """
        Getter for the power ups for a given mode

        :return: a list of differents power ups
        """
        pass
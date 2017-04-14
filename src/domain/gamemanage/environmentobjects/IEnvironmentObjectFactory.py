import abc
from src.utility.metaclasses import MetaAbstractSingleton


class IEnvironmentObjectFactory(metaclass=MetaAbstractSingleton):

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

        :return: a list of different power ups
        """
        pass
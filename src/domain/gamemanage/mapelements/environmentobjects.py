import abc

import src.domain.gamemanage.mapelements.obstacle as obstacle
import src.utility.metaclasses as metaclasses


class IEnvironmentObjectFactory(metaclass=metaclasses.MetaAbstractSingleton):
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


class ClassicEnvironmentObjectFactory(metaclass=metaclasses.MetaSingleton):
    def getDestructibleObstacles(self) -> list:
        destructibleexamples = list()
        destructibleexamples.append(obstacle.DestructibleObstacle())
        return destructibleexamples

    def getUndestructibleOstacles(self) -> list:
        undestructibleexamples = list()
        undestructibleexamples.append(obstacle.UndestructibleObstacle())
        return undestructibleexamples

    def getPowerUps(self) -> list:
        """
        Getter for the power ups for a given mode

        :return: a list of different power ups
        """
        pass

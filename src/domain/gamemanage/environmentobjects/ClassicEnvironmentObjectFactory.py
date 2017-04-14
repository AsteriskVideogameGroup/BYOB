from src.domain.gamemanage.obstacle import DestructibleObstacle, UndestructibleObstacle
from src.utility import MetaSingleton


class ClassicEnvironmentObjectFactory(metaclass=MetaSingleton):

    def getDestructibleObstacles(self) -> list:

        destructibleexamples = list()
        destructibleexamples.append(DestructibleObstacle())
        return destructibleexamples

    def getUndestructibleOstacles(self) -> list:

        undestructibleexamples = list()
        undestructibleexamples.append(UndestructibleObstacle())
        return undestructibleexamples

    def getPowerUps(self) -> list:
        """
        Getter for the power ups for a given mode

        :return: a list of different power ups
        """
        pass
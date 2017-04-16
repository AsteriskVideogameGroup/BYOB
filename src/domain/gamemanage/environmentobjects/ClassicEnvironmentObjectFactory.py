from src.utility.metaclasses import MetaSingleton


class ClassicEnvironmentObjectFactory(metaclass=MetaSingleton):

    def getDestructibleObstacles(self) -> list:
        import src.domain.gamemanage.obstacle.DestructibleObstacle as DestructibleObstacle

        destructibleexamples = list()
        destructibleexamples.append(DestructibleObstacle())
        return destructibleexamples

    def getUndestructibleOstacles(self) -> list:
        import src.domain.gamemanage.obstacle.UndestructibleObstacle as UndestructibleObstacle

        undestructibleexamples = list()
        undestructibleexamples.append(UndestructibleObstacle())
        return undestructibleexamples

    def getPowerUps(self) -> list:
        """
        Getter for the power ups for a given mode

        :return: a list of different power ups
        """
        pass
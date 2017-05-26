from src.domain.gamemanage.obstacle import IObstacle


class DestructibleObstacle(IObstacle):
    ########## ATTRIBUTES DEFINITION ##########
    # _position : Position

    def getPosition(self):
        """
        :return: the position of the obstacle
        """
        return self._position

    def setPosition(self, position):
        """
        Set the position of the obstacle
        :param position: the position to set
        """
        self._position = position

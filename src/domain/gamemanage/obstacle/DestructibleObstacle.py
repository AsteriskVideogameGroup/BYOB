from src.domain.gamemanage.obstacle.IObstacle import IObstacle


class DestructibleObstacle(IObstacle):

    ########## ATTRIBUTES DEFINITION ##########
    # _position : Position

    def getPosition(self) -> 'src.utility.geometrictools.Position':
        """
        :return: the position of the obstacle
        """
        return self._position

    def setPosition(self, position: 'src.utility.geometrictools.Position'):
        """
        Set the position of the obstacle
        :param position: the position to set
        """
        self._position = position


import src.utility.geometrictools.Position
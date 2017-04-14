from src.domain.gamemanage.obstacle import IObstacle
from src.utility.geometrictools import Position


class UndestructibleObstacle(IObstacle):

    ########## ATTRIBUTES DEFINITION ##########
    # _position : Position

    def getPosition(self) -> Position:
        """
        :return: the position of the obstacle
        """
        return self._position

    def setPosition(self, position: Position):
        """
        Set the position of the obstacle
        :param position: the position to set
        """
        self._position = position
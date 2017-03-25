from src.model.domain.obstacle.IObstacle import *


class UndestructibleObstacle(IObstacle):

    _position = None

    def getPosition(self) -> Position:
        return self._position

    def setPosition(self, position: Position):
        self._position = position

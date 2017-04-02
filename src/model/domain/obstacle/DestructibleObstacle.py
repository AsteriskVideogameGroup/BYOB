from src.model.domain.obstacle.IObstacle import *


class DestructibleObstacle(IObstacle):

    _position = None

    def getPosition(self) -> Position:
        return self._position

    def setPosition(self, position: Position):
        self._position = position


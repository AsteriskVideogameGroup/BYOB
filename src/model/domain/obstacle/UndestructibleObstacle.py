from src.model.domain.obstacle import IObstacle
from src.utility import Position


class UndestructibleObstacle(IObstacle):

    _position = None

    def getPosition(self) -> Position:
        return self._position

    def setPosition(self, position: Position):
        self._position = position

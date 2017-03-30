from src.model.domain.IMapElement import *


class CorrectedBoB (IMapElement):

    _position = None

    def __init__(self):
        self._position = None

    def setPosition(self, position: Position):
        self._position = position

    def getPosition(self) -> Position:
        return self._position

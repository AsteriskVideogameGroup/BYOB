from src.model.domain.IMapElement import *
from src.model.domain.BoB import BoBDescription
from src.model.domain.Player import Player

class BoB (IMapElement):

    _descr = None
    _owner = None
    _bobnameid = None
    _position = None


    def __init__(self, descr: BoBDescription, owner: Player):
        self._position = None
        self._descr = descr
        self._owner = owner

    def setPosition(self, position: Position):
        self._position = position

    def getPosition(self) -> Position:
        return self._position

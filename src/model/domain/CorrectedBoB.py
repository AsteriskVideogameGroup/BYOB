from src.model.domain.IMapElement import *

#TODO Chiarire perchè non viene accettato il file BoB.py negli import e rimuovere commento qui e in BoB.py
class BoB (IMapElement):

    _position = None

    def __init__(self):
        self._position = None

    def setPosition(self, position: Position):
        self._position = position

    def getPosition(self) -> Position:
        return self._position

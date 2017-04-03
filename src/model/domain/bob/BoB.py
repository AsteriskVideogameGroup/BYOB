from src.model.domain.IMapElement import *
from src.model.domain.BoB import BoBDescription
from src.model.domain.Player import Player

class BoB (IMapElement):

    ########## ATTRIBUTES DEFINITION ##########
    # _descr : BoBDescription
    # _owner : Player
    # _bobnameid : Str
    # _position : Position


    def __init__(self, descr: BoBDescription, owner: Player):
        """
        :param descr: Bundle of stats for the BoBs
        :param owner: Player who owns the BoB
        """
        self._position = None
        self._descr = descr
        self._owner = owner

    def setPosition(self, position: Position):
        """
        Set the position of BoB into the map
        :param position: position to set
        """
        self._position = position

    def getPosition(self) -> Position:
        """
        :return: the position of the BoB into the map 
        """
        return self._position

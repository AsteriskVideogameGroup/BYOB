from src.domain.gamemanage.gameessentials.IMapElement import IMapElement


class BoB(IMapElement):
    ########## ATTRIBUTES DEFINITION ##########
    # _descr : BoBDescription
    # _owner : Player
    # _bobnameid : Str
    # _position : Position


    def __init__(self, descr, owner):
        """
        :param descr: Bundle of stats for the BoBs
        :param owner: Player who owns the BoB
        """
        self._position = None
        self._descr = descr
        self._owner = owner

    def setPosition(self, position):
        """
        Set the position of BoB into the map
        :param position: position to set
        """
        self._position = position

    def getPosition(self):
        """
        :return: the position of the BoB into the map 
        """
        return self._position

    def getOwner(self):
        return self._owner

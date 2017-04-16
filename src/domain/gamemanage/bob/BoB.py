import src.domain.gamemanage.gameessentials.IMapElement as IMapElement


class BoB(IMapElement):

    ########## ATTRIBUTES DEFINITION ##########
    # _descr : BoBDescription
    # _owner : Player
    # _bobnameid : Str
    # _position : Position



    def __init__(self, descr: 'src.domain.gamemanage.bob.BoBDescription', owner: 'src.domain.gamemanage.player.Player'):
        """
        :param descr: Bundle of stats for the BoBs
        :param owner: Player who owns the BoB
        """
        self._position = None
        self._descr = descr
        self._owner = owner

    def setPosition(self, position: 'src.utility.geometrictools.Position'):
        """
        Set the position of BoB into the map
        :param position: position to set
        """
        self._position = position

    def getPosition(self) -> 'src.utility.geometrictools.Position':
        """
        :return: the position of the BoB into the map 
        """
        return self._position

import src.domain.gamemanage.bob.BoBDescription
import src.domain.gamemanage.player.Player
import src.utility.geometrictools.Position

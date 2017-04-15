import src.domain.gamemanage.gameessentials as gameessentials
import src.domain.gamemanage.player as player
import src.utility.geometrictools as geometrictools
import src.utility.metaclasses as metaclasses



class BoB(gameessentials.IMapElement):
    ########## ATTRIBUTES DEFINITION ##########
    # _descr : BoBDescription
    # _owner : Player
    # _bobnameid : Str
    # _position : Position


    def __init__(self, descr: BoBDescription, owner: player.Player):
        """
        :param descr: Bundle of stats for the BoBs
        :param owner: Player who owns the BoB
        """
        self._position = None
        self._descr = descr
        self._owner = owner

    def setPosition(self, position: geometrictools.Position):
        """
        Set the position of BoB into the map
        :param position: position to set
        """
        self._position = position

    def getPosition(self) -> geometrictools.Position:
        """
        :return: the position of the BoB into the map 
        """
        return self._position


class BoBBuilder(metaclass=metaclasses.MetaSingleton):
    def createBoB(self, bobnameid: str, owner: player.Player) -> BoB:
        """
        Building of the BoB
        :param bobnameid: id of the BoB chosen by the player
        :param owner: player who choose the BoB
        :return: the BoB built in this way
        """

        descr = BoBCatalog().getBoBByID(bobnameid)
        newbob = BoB(descr, owner)
        return newbob


class BoBCatalog(metaclass=metaclasses.MetaSingleton):
    def getBoBByID(self, bobnameid):
        return BoBDescription

    def BoBCatalog(self):
        pass

    def getInstance(self):
        return BoBCatalog


class BoBDescription(metaclass=metaclasses.MetaSingleton):
    ########## ATTRIBUTES DEFINITION ##########
    # _descr:

    def getDescription(self):
        return self._descr

from src.domain.gamemanage.bob import BoB, BoBCatalog
from src.domain.gamemanage.player import Player
from src.utility.metaclasses import MetaSingleton


class BoBBuilder(metaclass=MetaSingleton):

    def createBoB(self, bobnameid: str, owner: Player) -> BoB:
        """
        Building of the BoB
        :param bobnameid: id of the BoB chosen by the player
        :param owner: player who choose the BoB
        :return: the BoB built in this way
        """

        descr = BoBCatalog().getBoBByID(bobnameid)
        newbob = BoB(descr, owner)
        return newbob
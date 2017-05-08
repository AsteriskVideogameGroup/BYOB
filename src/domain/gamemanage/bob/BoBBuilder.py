from src.domain.gamemanage.bob.BoB import BoB
from src.domain.gamemanage.bob.BoBCatalog import BoBCatalog
from src.utility.metaclasses import MetaSingleton


class BoBBuilder(metaclass=MetaSingleton):

    def createBoB(self, bobnameid: str, owner):
        """
        Building of the BoB
        :param bobnameid: id of the BoB chosen by the player
        :param owner: player who choose the BoB
        :return: the BoB built in this way
        """

        descr = BoBCatalog().getBoBByID(bobnameid)
        newbob = BoB(descr, owner)
        return newbob
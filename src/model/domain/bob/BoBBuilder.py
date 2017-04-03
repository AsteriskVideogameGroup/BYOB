from src.utility import MetaSingleton
from src.model.domain.BoB import BoBCatalog, BoB
from src.model.domain.Player import Player

class BoBBuilder(metaclass=MetaSingleton):

    def createBoB(self, bobnameid: str, owner: Player) -> BoB:
        """
        :param bobnameid: 
        :param owner: 
        :return: 
        """
        #TODO angelo commenta pd

        descr = BoBCatalog().getBoBByID(bobnameid)
        newbob = BoB(descr, owner)
        return newbob



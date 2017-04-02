from src.utility import MetaSingleton
from src.model.domain.bob import BoBCatalog, BoBDescription, BoB
from src.model.domain.Player import Player

class BoBBuilder(metaclass=MetaSingleton):

    def createBoB(self, bobnameid: str, owner: Player):
        descr = BoBCatalog.getBoBByID(bobnameid)
        newbob = BoB.create(descr, owner)
        return newbob



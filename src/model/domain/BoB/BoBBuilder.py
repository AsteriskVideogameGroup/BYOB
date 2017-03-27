from src.utility.MetaSingleton import MetaSingleton
from src.model.domain.BoB import BoBCatalog
from src.model.domain.BoB import BoBDescription
from src.model.domain import BoB

class BoBBuilder(metaclass=MetaSingleton):

    def BoBBuilder(self):
        pass

    def createBob(self, bobnameid, owner):
        descr = BoBCatalog.getBoBByID(bobnameid)
        create(descr, owner)
        return descr

    def getInstance(self):
        return BoBBuilder




from src.utility.Singleton import Singleton
from src.model.domain.BoB import BoBCatalog
from src.model.domain.BoB import BoBDescription
from src.model.domain import BoB

class BoBBuilder(metaclass=Singleton):

    def BoBBuilder(self):
        pass

    def createBob(self, bobnameid, owner):
        descr = BoBCatalog.getBoBByID(bobnameid)
        create(descr, owner)
        return descr

    def getInstance(self):
        return BoBBuilder




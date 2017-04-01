from src.utility import MetaSingleton
from src.model.domain.bob import BoBCatalog, BoBDescription, BoB

class BoBBuilder(metaclass=MetaSingleton):

    def BoBBuilder(self):
        pass

    def createBob(self, bobnameid, owner):
        descr = BoBCatalog.getBoBByID(bobnameid)
        create(descr, owner)
        return descr

    def getInstance(self):
        return BoBBuilder




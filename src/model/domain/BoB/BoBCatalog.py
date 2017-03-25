from src.utility.Singleton import Singleton
from src.model.domain.BoB import BoBDescription


class BoBCatalog(metaclass=Singleton):

    def getBoBByID(self, bobnameid):
        return BoBDescription

    def BoBCatalog(self):
        pass

    def getInstance(self):
        return BoBCatalog
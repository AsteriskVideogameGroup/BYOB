from src.utility.MetaSingleton import MetaSingleton
from src.model.domain.bob import BoBDescription


class BoBCatalog(metaclass=MetaSingleton):

    def getBoBByID(self, bobnameid):
        return BoBDescription

    def BoBCatalog(self):
        pass

    def getInstance(self):
        return BoBCatalog
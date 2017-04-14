from src.domain.gamemanage.bob import BoBDescription
from src.utility.metaclasses.MetaSingleton import MetaSingleton


class BoBCatalog(metaclass=MetaSingleton):

    def getBoBByID(self, bobnameid):
        return BoBDescription

    def BoBCatalog(self):
        pass

    def getInstance(self):
        return BoBCatalog
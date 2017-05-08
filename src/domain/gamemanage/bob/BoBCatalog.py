from src.domain.gamemanage.bob import BoBDescription
from src.utility.metaclasses.MetaSingleton import MetaSingleton


class BoBCatalog(metaclass=MetaSingleton):

    def getBoBByID(self, bobnameid: str):
        return BoBDescription(bobnameid)

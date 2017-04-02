from src.utility.MetaSingleton import MetaSingleton
from src.model.domain.BoB import BoBDescription


class BoBCatalog(metaclass=MetaSingleton):

    def getBoBByID(self, bobnameid):
        descr = BoBDescription.getDescription(bobnameid)
        return descr


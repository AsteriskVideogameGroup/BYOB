from src.utility.MetaSingleton import MetaSingleton
from src.model.domain.BoB import BoBDescription


class BoBCatalog(metaclass=MetaSingleton):

    def getBoBByID(self, bobnameid: str) -> BoBDescription:
        #TODO tradurre descr e aggingre parametri
        # TODO fare con multiton?
        descr = BoBDescription()
        return descr


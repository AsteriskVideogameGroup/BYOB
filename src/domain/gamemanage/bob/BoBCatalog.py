from src.utility.metaclasses.MetaSingleton import MetaSingleton


class BoBCatalog(metaclass=MetaSingleton):

    def getBoBByID(self, bobnameid: str):
        import src.domain.gamemanage.bob.BoBDescription as BoBDescription
        return BoBDescription(bobnameid)

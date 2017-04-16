from src.utility.metaclasses import MetaSingleton


class BoBBuilder(metaclass=MetaSingleton):

    def createBoB(self, bobnameid: str, owner: 'src.domain.gamemanage.player.Player') -> 'src.domain.gamemanage.bob.BoB':
        """
        Building of the BoB
        :param bobnameid: id of the BoB chosen by the player
        :param owner: player who choose the BoB
        :return: the BoB built in this way
        """

        import src.domain.gamemanage.bob.BoBCatalog as BoBCatalog
        import src.domain.gamemanage.bob.BoB as BoB

        descr = BoBCatalog().getBoBByID(bobnameid)
        newbob = BoB(descr, owner)
        return newbob


import src.domain.gamemanage.player.Player
class GameHandler:

    ########## ATTRIBUTES DEFINITION ##########
    # _currentgame : Game
    # _started : Bool

    def __init__(self, newgame: 'src.domain.gamemanage.gameessentials.Game'):
        """
        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._started = False

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._started = self._currentgame.startGame()

    def chooseBoB(self, owner: 'src.domain.gamemanage.player.Player', bobnameid: str = 'default'):
        """
        Let the player choose his BoB
        :param owner: Player who choose the BoB
        :param bobnameid: Name id of the chosen BoB
        """

        import src.domain.gamemanage.bob.BoBBuilder as BoBBuilder

        newbob = BoBBuilder().createBoB(bobnameid, owner)
        self._currentgame.addBoB(newbob)


import src.domain.gamemanage.gameessentials.Game
import src.domain.gamemanage.player.Player

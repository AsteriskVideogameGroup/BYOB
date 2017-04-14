from src.model.domain import Game, Player

from src.domain.gamemanage.bob import BoBBuilder


class GameHandler:

    ########## ATTRIBUTES DEFINITION ##########
    # _currentgame : Game
    # _started : Bool

    def __init__(self, newgame: Game):
        """
        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._started = False

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._started = self._currentgame.startGame()

    def chooseBoB(self, owner: Player, bobnameid: str = 'default'):
        """
        Let the player choose his BoB
        :param owner: Player who choose the BoB
        :param bobnameid: Name id of the chosen BoB
        """
        newbob = BoBBuilder().createBoB(bobnameid, owner)
        self._currentgame.addBoB(newbob)
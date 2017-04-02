from src.model.domain.BoB import BoBBuilder
from src.model.domain import Game
from src.model.domain.Player import Player


class GameHandler:

    _currentgame = None
    _started = None
    _newbob = None

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
        """ Choose BoB before game start """
        self._newbob = BoBBuilder.createBoB(owner, bobnameid)
        Game.addBoB(self._newbob)
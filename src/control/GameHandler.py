from src.model.domain.bob import BoBBuilder
from src.model.domain import Game
from src.utility import MetaSingleton


class GameHandler(metaclass=MetaSingleton):

    _currentgame = None
    _started = None

    def __init__(self, newgame):
        """

        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._started = False

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._started = self._currentgame.startGame()

    def chooseBoB(self, bobnameid, owner):
        newbob = BoBBuilder.createBob(bobnameid, owner)
        addBoB(newbob)

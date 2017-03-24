from src.model.domain.Game import *


class GameHandler:

    _currentgame = None
    _started = None

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

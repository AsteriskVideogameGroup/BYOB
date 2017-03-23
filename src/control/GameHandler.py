from src.model.domain.Game import *


class GameHandler:

    _currentgame = None

    def __init__(self, newgame: Game):
        """

        :param newgame: Game object to handle
        """
        self._currentgame = newgame

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()

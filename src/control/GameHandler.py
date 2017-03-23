from src.model.Game import *

class GameHandler:

    _currentgame = None

    def __init__(self, newgame: Game):
        self._currentgame = newgame

    def prepareGame(self):
        self._currentgame.prepareGame()

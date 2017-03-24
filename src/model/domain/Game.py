from src.model.domain.Map import *
from src.model.domain.Room import *
from src.model.domain.gamemode.IGameMode import *
from src.model.factories.StrategyFactory import *
from src.model.domain.BoB import *
import time

class Game:

    _gameroom = None
    _currentmode = None
    _bobarray = None
    _gamemap = None
    _endgametime = None

    def __init__(self, playerroom: Room, gamemode: IGameMode):
        """

        :param playerroom: virtual room for the players of the game
        :param gamemode: game mode of the game
        """

        self._gameroom = playerroom
        self._currentmode = gamemode

    def addBoB(self, newbob: BoB):
        """
        Add a BoB to the game

        :param newbob: BoB that must be added to the game
        """
        self._bobarray.append(newbob)

    def prepareGame(self):
        """
        Prepare the game for the start

        """

        dims = self._currentmode.getMapDimensions()
        envobj = self._currentmode.getEnvironmentObjectFactory()
        invtime = self._currentmode.getInvulnerabilityTime()

        algo = StrategyFactory.getInstance().getMapStrategy()

        self._gamemap = Map(envobj, invtime)
        self._gamemap.setBoBs(self._bobarray)
        self._gamemap.setDimensions(dims)
        self._gamemap.setMapStrategy(algo)
        self._gamemap.prepareMap()

    def startGame(self) -> bool:
        """
        Start the game computing the end time.

        :return: True signaling the start to gamehandler
        """

        duration = self._currentmode.getDuration()
        starttime = time.time()
        self.endgametime = starttime + duration*60
        return True








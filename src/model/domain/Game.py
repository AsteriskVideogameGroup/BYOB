from src.model.domain import Map, Room
from src.model.domain.BoB import BoB
from src.model.domain.gamemode import Mode
from src.model.factories import StrategyFactory
import time


class Game:

    _gameroom = None
    _currentmode = None
    _bobarray = None
    _gamemap = None

    def __init__(self, playerroom: Room, gamemode: Mode):
        """
        :param playerroom: virtual room for the players of the game
        :param gamemode: game mode of the game
        """

        self._gameroom = playerroom
        self._currentmode = gamemode

    def addBoB(self, newbob):
        """
        Add a bob to the game
        :param newbob: bob that must be added to the game
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
        # TODO: in visual paradigm dovremmo aggiornare la questione della strategy
        # sembra legittimo mettere come parametri per il costruttore la factory
        # degli elementi e la strategia di disposizione

        self._gamemap = Map(envobj, algo)

        self._gamemap.setInvulnerabilityTime(invtime)
        self._gamemap.setBoBs(self._bobarray)
        self._gamemap.setDimensions(dims)
        self._gamemap.prepareMap()

    def startGame(self) -> bool:
        """
        Start the game computing the end time.

        :return: True signaling the start to gamehandler
        """

        duration = self._currentmode.getDuration()
        self.endgametime = time.time() + duration*60
        return True








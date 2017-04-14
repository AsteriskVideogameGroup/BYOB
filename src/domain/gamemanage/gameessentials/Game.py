import time

from src.domain.gamemanage.gameessentials import Map
from src.domain.gamemanage.gamemode import Mode
from src.domain.gamemanage.player import Room


class Game:

    ########## ATTRIBUTES DEFINITION ##########
    # _gameroom : Room
    # _currentmode : Mode
    # _bobarray : list (of BoBs)
    # _gamemap : Map
    # _endgametime : time.Time()

    def __init__(self, playerroom: Room, gamemode: Mode):
        """
        :param playerroom: virtual room for the players of the game
        :param gamemode: game mode of the game
        """

        self._gameroom = playerroom
        self._currentmode = gamemode
        self._bobarray = list()

    def addBoB(self, newbob):
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

        algo = self._currentmode.getMapStrategy()
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
        self._endgametime = time.time() + duration*60
        return True


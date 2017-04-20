import time
import copy



class Game:

    ########## ATTRIBUTES DEFINITION ##########
    # _gameroom : Room
    # _currentmode : Mode
    # _bobarray : list (of BoBs)
    # _gamemap : Map
    # _endgametime : time.Time()

    def __init__(self, playerroom: 'src.domain.gamemanage.player.Room', gamemode: 'src.domain.gamemanage.gamemode.Mode'):
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

        import src.domain.gamemanage.gameessentials.Map as Map

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

    def getBoBArray(self) -> list:
        return self._bobarray

    def getMode(self) -> 'src.domain.gamemanage.gamemode.Mode':
        return self._currentmode

    def getRoom(self) -> 'src.domain.gamemanage.player.Room':
        return self._gameroom


import src.domain.gamemanage.player.Room
import src.domain.gamemanage.gamemode.Mode
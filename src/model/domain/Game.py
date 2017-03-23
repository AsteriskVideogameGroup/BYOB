from src.model.domain.Map import *
from src.model.domain.Room import *
from src.model.domain.gamemode.IGameMode import *


class Game:

    _gameroom = None
    _currentmode = None
    _bobarray = None

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
        gamemap = Map(envobj, invtime)


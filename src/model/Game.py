from src.model.Room import *
from src.model.IGameMode import *
from src.model.Map import *
from src.model.BoB import *

class Game:

    _gameroom = None
    _currentmode = None
    _bobarray = None

    def __init__(self, playerroom: Room, gamemode: IGameMode):
        self._gameroom = playerroom
        self._currentmode = gamemode

    def addBoB(self, newbob: BoB):
        self._bobarray.append(newbob)

    def prepareGame(self):
        dims = self._currentmode.getMapDimensions()
        envobj = self._currentmode.getEnvironmentObjectFactory()
        invtime = self._currentmode.getInvulnerabilityTime()
        gamemap = Map(envobj, invtime)


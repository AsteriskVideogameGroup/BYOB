import time

from src.model.domain import Map, Room
from src.model.domain.environmentgamemode.gamemode import Mode


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

        algo = StrategyFactory.getInstance().getMapStrategy()

        # TODO StrategyFactory cancellata!!!
        # from src.utility import MetaSingleton, GlobalSettings
        #     # class StrategyFactory(metaclass=MetaSingleton):
        #     # TODO CANCELLARE LA CLASSE, LA LETTURA DELLA MAP STRATEGY è nella MODALITÀ
        #         #     def getMapStrategy(self):
        #         """
        #         Takes, from configuration, the map strategy that must be used
        #         :return: the map strategy that must be used
        #         """
        #         MAPSTRATEGY = 'mapstrategy'
        #         mapstrategyname = GlobalSettings().getSetting(MAPSTRATEGY)
        #         mapstrategy = globals()[mapstrategyname]
        #         self._mapstrategy = mapstrategy
        #         return self._mapstrategy


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








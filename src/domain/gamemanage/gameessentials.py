import abc

import time
import typing as List

import src.domain.gamemanage.player as player
import src.domain.gamemanage.environmentobjects as environmentobjects
import src.domain.gamemanage.gamemode as gamemode
import src.utility.geometrictools as geometrictools
import src.utility.mapstrategy as mapstrategy


class Game:
    ########## ATTRIBUTES DEFINITION ##########
    # _gameroom : Room
    # _currentmode : Mode
    # _bobarray : list (of BoBs)
    # _gamemap : Map
    # _endgametime : time.Time()

    def __init__(self, playerroom: player.Room, gamemode: gamemode.Mode):
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
        self._endgametime = time.time() + duration * 60
        return True


class IMapElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setPosition(self, position: geometrictools.Position):
        """
        Set the position for the element
        :param position: position to set
        """

        pass

    @abc.abstractmethod
    def getPosition(self) -> geometrictools.Position:
        """
        Getter of the position of the element
        :return: element's position
        """

        pass


class Map:
    ########## ATTRIBUTES DEFINITION ##########

    # _envobjfactory : IEnvironmentObjectFactory
    # _invtime : int
    # _dimensions : Dimensions
    # _poweruparray : list (of IPowerUP)
    # _strategy : IMapStrategy
    # _placablepowups : list (of IPowerUp)

    # _bobarray : list (of BoB)
    # _undstrobstaclearray : list (of UndestructibleArray)
    # _dstrobstaclearray :  list (of DestructibleArray)

    # Dictionary that records the occupied positions (structure = (position,element) )
    # _occupiedpositions : dict

    # TODO RIMUOVERE QUESTO COSTRUTTORE, UTILIZZATO SOLO PER TESTING
    # def __init__(self, strategy: IMapStrategy):
    #    self._strategy = strategy
    #    self._occupiedpositions = {}

    def __init__(self, envobjfactory: environmentobjects.IEnvironmentObjectFactory, strategy: mapstrategy.IMapStrategy):
        self._envobjfactory = envobjfactory
        self._strategy = strategy
        self._occupiedpositions = {}

    def setMapStrategy(self, mapstrategy: mapstrategy.IMapStrategy):
        """
        Setting of the positioning algorithm
        :param mapstrategy: algorithm for the positioning of the map elements:
        """
        self._strategy = mapstrategy

    def setDimensions(self, dimensions: geometrictools.Dimensions):
        """
        Set the dimensions for the map (number of tiles for width and for height)
        :param dimensions: dimensions to set
        """
        self._dimensions = dimensions

    def setBoBs(self, bobs: list):
        """
        Set BoBs to the map
        :param bobs: BoBs to set
        """
        self._bobarray = bobs

    def setInvulnerabilityTime(self, invtime: int):
        """
        Set invulnerability when receiving damage
        :param invtime: time of invulnerability in seconds
        """
        self._invtime = invtime

    def prepareMap(self):
        """
        Disposing of elements on the map
        """

        samplesDestrObstacle = self._envobjfactory.getDestructibleObstacles()
        samplesUndestrObstacle = self._envobjfactory.getUndestructibleOstacles()

        # self._placeablepowups = self._envobjfactory.getPowerUps()

        undstrarraytoset = self._strategy.disposeUndestrObstacles(samplesUndestrObstacle, self._dimensions)
        self.setUndstrObstacleArray(undstrarraytoset)

        # Unlike obstacles, the bobs setter doesn't occupy the position
        # so it must be occupied during preparemap()
        self._strategy.disposeBoBs(self._bobarray, self._dimensions)
        self._occupyElementsPositions(self._bobarray)

        dstrarraytoset = self._strategy.disposeDestrObstacles(samplesDestrObstacle, self._dimensions, self._bobarray)
        self.setDstrObstacleArray(dstrarraytoset)

    def getDimensions(self):
        """
        Getter of map dimensions
        :return: the map dimensions
        """

        return self._dimensions

    def isOccupied(self, position: geometrictools.Position):
        """
        Check if the position is occupied
        :param position: position to check
        :return: True if occupied, False if free
        """

        return (position in self._occupiedpositions)

    def setUndstrObstacleArray(self, undstrarray: list):
        """
        Set a list of undestructible obstacles and occupy their position
        :param undstrarray: list to set
        """

        self._undstrobstaclearray = undstrarray
        self._occupyElementsPositions(undstrarray)

    def setDstrObstacleArray(self, dstrarray: list):
        """
        Set a list of destructible obstacles and occupy their position
        :param dstrarray: list to set
        """

        self._dstrobstaclearray = dstrarray
        self._occupyElementsPositions(dstrarray)

    def _occupyElementsPositions(self, imapelements: list):
        """
        Occupy the positions of a given IMapElements list
        :param imapelements: list of IMapElements that must occupy a position
        """
        for ele in imapelements:
            self._occupyPosition(ele)

    def _occupyPosition(self, mapelement: IMapElement):
        """
        Occupy the position of element in the inner dictionary for the occupied positions
        :param mapelement: map element occuping a position
        """

        self._occupiedpositions[mapelement.getPosition()] = mapelement


class MatchMaker:
    _modes = dict()  # singleton instance

    def __new__(cls, *args, **kwargs) -> 'MatchMaker':
        if cls._modes.get(args[0], None) is None:
            mode = gamemode.GameModeFactory().getGameMode(args[0])  # translate gamemode ID to IGameMode
            newmatchmaker = super().__new__(cls)  # instantiate new Matchmaker
            newmatchmaker._mode = mode  # assign a mode to the matchmaker
            newmatchmaker._unrankedqueue = list()
            newmatchmaker._rankedqueue = list()
            cls._modes[args[0]] = newmatchmaker  # add newmatchmaker into the dict

        return cls._modes.get(args[0])

    @classmethod
    def getInstance(cls, gamemode: str) -> 'MatchMaker':
        """
        Gives an instance of the matchmaker suitable for the selected GameMode
        :param gamemode: String ID of the GameMode
        :return: The selected matchmaker for the GameMode
        """
        return cls.__new__(cls(), gamemode)

    def pushPlayer(self, client: player.ClientInfos, isranked: bool):
        """
        Add a Client to the list of the availables
        :param client: Client of the Player who wants to join a game
        :param isranked: Specifies if the Game is ranked
        """
        if isranked is True:
            # TODO non facciamo le ranked
            self._rankedqueue.append(client)
            self._rankedqueue.sort()
            # TODO controllare associazione giocatori
        else:
            self._unrankedqueue.append(client)  # add client to the list
            self._extractClients(self._unrankedqueue)

    def _extractClients(self, queue: List[player.ClientInfos]):
        maxplayer = self._mode.getMaxPlayers()  # maxplayers depends on the GameMode
        if len(queue) >= maxplayer:

            print("Room pronta con " + str(len(queue)) + " gioacatori")  # TODO rimuovi

            playerroom = player.Room()  # bundle of player that will play
            arrclients = list()  # list of the selected players

            for i in range(0, maxplayer):
                client = queue.pop(0)
                playerroom.addPlayer(client.player)
                arrclients.append(client)

            # TODO da completare quando la Map sarà corretta

            newgame = Game(playerroom, self._mode)  # instantiate the new game
            ghandle = GameHandler(newgame)  # creates the new controller for the clients

            for client in arrclients:  # update all client observers
                client.update(ghandle)

# TODO vedi dove deve andare
class GameHandler:
    ########## ATTRIBUTES DEFINITION ##########
    # _currentgame : Game
    # _started : Bool

    def __init__(self, newgame: gameessentials.Game):
        """
        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._started = False

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._started = self._currentgame.startGame()

    def chooseBoB(self, owner: player.Player, bobnameid: str = 'default'):
        """
        Let the player choose his BoB
        :param owner: Player who choose the BoB
        :param bobnameid: Name id of the chosen BoB
        """
        newbob = bob.BoBBuilder().createBoB(bobnameid, owner)
        self._currentgame.addBoB(newbob)
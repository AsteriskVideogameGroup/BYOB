from src.model.domain import IMapElement
from src.model.domain.environmentobject.factory import IEnvironmentObjectFactory
from src.utility import Dimensions, Position
from src.utility.mapstrategy import IMapStrategy


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

    #TODO RIMUOVERE QUESTO COSTRUTTORE, UTILIZZATO SOLO PER TESTING
    #def __init__(self, strategy: IMapStrategy):
    #    self._strategy = strategy
    #    self._occupiedpositions = {}

    def __init__(self, envobjfactory: IEnvironmentObjectFactory, strategy: IMapStrategy):

        self._envobjfactory = envobjfactory
        self._strategy = strategy
        self._occupiedpositions = {}

    def setMapStrategy(self, mapstrategy: IMapStrategy):
        """
        Setting of the positioning algorithm

        :param mapstrategy: algorithm for the positioning of the map elements:
        """
        self._strategy = mapstrategy

    def setDimensions(self, dimensions: Dimensions):
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

        #self._placeablepowups = self._envobjfactory.getPowerUps()

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

    def isOccupied(self, position: Position):
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

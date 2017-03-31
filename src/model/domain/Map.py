from src.model.factories.IEnvironmentObjectFactory import IEnvironmentObjectFactory

from src.utility import Dimensions, Position
from src.utility.mapstrategy import IMapStrategy
from src.model.domain import IMapElement


class Map:

    _envobjfactory = None
    _invtime = None
    _dimensions = None
    _poweruparray = None
    _strategy = None
    _placablepowups = None

    _bobarray = None
    _undstrobstaclearray = None

    # Dictionary that records the occupied positions (structure = (position,element) )
    _occupiedpositions = None

    #TODO RIMUOVERE QUESTO COSTRUTTORE, UTILIZZATO SOLO PER TESTING
    def __init__(self):
        self._occupiedpositions = {}

    #TODO TOGLIERE I COMMENTI A QUESTO COSTRUTTORE
    #def __init__(self, envobjfactory: IEnvironmentObjectFactory, invtime: int):

    #    self._envobjfactory = envobjfactory
    #    self._invtime = invtime
    #    self._occupiedpositions = {}

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

    def prepareMap(self):
        """
        Disposing of elements on the map
        """

        samplesDestrObstacle = self._envobjfactory.getDestructibleObstacles()
        samplesUndestrObstacle = self._envobjfactory.getUndestructibleOstacles()
        self._placeablepowups = self._envobjfactory.getPowerUps()

        self.setUndstrObstacleArray(self._strategy.disposeUndestrObstacles(samplesUndestrObstacle, self._dimensions))

        # Unlike obstacles, the bobs setter doesn't occupy the position
        # so it must be occupied during preparemap()
        self._strategy.disposeBoBs(self._bobarray, self._dimensions)
        self._occupyElementsPositions(self._bobarray)


        #self._strategy.disposeDestrObstacles(self, samplesDestrObstacle)

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

    def _occupyElementsPositions(self, imapelements: list):
        for ele in imapelements:
            self._occupyPosition(ele)

    def _occupyPosition(self, mapelement: IMapElement):
        """
        Occupy the position of element in the inner dictionary for the occupied positions
        :param mapelement: map element occuping a position
        """

        self._occupiedpositions[mapelement.getPosition()] = mapelement

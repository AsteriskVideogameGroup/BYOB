# from src.model.factories.IEnvironmentObjectFactory import IEnvironmentObjectFactory
from src.utility import Dimensions, Position
from src.utility.mapstrategy import CorrectedIMapStrategy
from src.model.domain import IMapElement


class Map:
    def __init__(self):
        self._occupiedpositions = dict()

    def setMapStrategy(self, mapstrategy: CorrectedIMapStrategy):
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

        # samplesDestrObstacle = self._envobjfactory.getDestructibleObstacles()
        # samplesUndestrObstacle = self._envobjfactory.getUndestructibleOstacles()
        # self._placeablepowups = self._envobjfactory.getPowerUps()

        # self._strategy.disposeUndestrObstacles(self, samplesUndestrObstacle)

        # place BoBs on the Map
        listbobpositions = self._strategy.disposeBoBs(self, self._bobarray, self._dimensions)
        self.occupyPositions(listbobpositions)

        # self._strategy.disposeDestrObstacles(self, samplesDestrObstacle)

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
        for ele in undstrarray:
            self.occupyPosition(ele)

    def occupyPosition(self, mapelement: IMapElement):
        """
        Occupy the position of element in the inner dictionary for the occupied positions
        :param mapelement: map element occuping a position
        """

        self._occupiedpositions[mapelement.getPosition()] = mapelement

    def occupyPositions(self, mapelements: list):
        for singleelement in mapelements:
            self.occupyPosition(singleelement)

from src.model.factories.IEnvironmentObjectFactory import *
from src.utility.Dimensions import *
from src.utility.mapstrategy.IMapStrategy import *
from src.model.domain.IMapElement import *

class Map:

    _envobjfactory = None
    _invtime = None
    _dimensions = None
    _bobarray = None
    _strategy = None

    def __init__(self, envobjfactory: IEnvironmentObjectFactory, invtime: int):

        self._envobjfactory = envobjfactory
        self._invtime = invtime

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
        samplesDestrObstacle = self._envobjfactory.getDestructibleObstacles()
        samplesUndestrObstacle = self._envobjfactory.getUndestructibleOstacles()
        samplesPowerUps = self._envobjfactory.getPowerUps()

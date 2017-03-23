from src.model.domain.BoB import *
from src.model.factories.IEnvironmentObjectFactory import *
from src.utility.Dimensions import *


class Map:

    _envobjfactory = None
    _invtime = None
    _dimensions = None
    _bobarray = None

    def __init__(self, envobjfactory: IEnvironmentObjectFactory, invtime: int):
        self._envobjfactory = envobjfactory
        self._invtime = invtime

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
        pass
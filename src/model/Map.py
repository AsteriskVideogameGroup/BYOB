from src.model.IEnvironmentObjectFactory import *
from src.model.BoB import *
from src.utile.Dimensions import *

class Map:

    _envobjfactory = None
    _invtime = None
    _dimensions = None
    _bobarray = None

    def __init__(self, envobjfactory: IEnvironmentObjectFactory, invtime: int):
        self._envobjfactory = envobjfactory
        self._invtime = invtime

    def setDimensions(self, dimensions: Dimensions):
        self._dimensions = dimensions

    def setBoBs(self, bobs: list[BoB]):
        self._bobarray = bobs


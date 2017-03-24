from src.utility.mapstrategy.IMapStrategy import *
from src.model.domain.Map import *
from src.model.domain.IMapElement import *
import copy

class FirstMapStrategy(IMapStrategy):

    def __init__(self):
        pass

    def disposeDestrObstacles(self, map: Map, dstrobstacles: list) -> Map:
        #TODO
        pass

    def disposeUndestrObstacles(self, map: Map, undstrobstacles: list) -> Map:
        #TODO
        pass

    def disposeBoBs(self, map: Map, bobs: list) -> Map:
        #TODO
        pass

    def disposePowerUps(self, map: Map, powerups: list) -> Map:
        #TODO
        pass

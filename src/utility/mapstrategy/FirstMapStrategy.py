from src.utility.mapstrategy.IMapStrategy import *
from src.model.domain.Map import *
from src.model.domain.IMapElement import *
import copy
import random

class FirstMapStrategy(IMapStrategy):

    def __init__(self):
        pass

    def disposeDestrObstacles(self, map: Map, dstrobstacles: list) -> Map:
        #TODO
        pass

    def disposeUndestrObstacles(self, map: Map, undstrobstacles: list) -> Map:
        """
        Dispose undestructible obstacles inside a map

        :param map: map where the obstacles must be placed
        :param undstrobstacles: list of different sample of undestructible obstacles that must be placed
        :return:
        """
        dim = map.getDimensions()
        height = dim.getHeight()
        width = dim.getWidth()

        undstrarray = []

        for i in range (1,height):
            if i%2 == 0:
                for j in range (1,width):
                    if j%2 == 0:
                        newundstr = copy.deepcopy(random.choice(undstrobstacles))
                        newundstr.setPosition(i,j)
                        undstrarray.append(newundstr)

        map.setUndstrObstacleArray(undstrarray)

    def disposeBoBs(self, map: Map, bobs: list) -> Map:
        #TODO
        pass

    def disposePowerUps(self, map: Map, powerups: list) -> Map:
        #TODO
        pass

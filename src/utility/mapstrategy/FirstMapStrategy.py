from src.utility.mapstrategy.IMapStrategy import *
from src.model.domain.Map import *
from src.model.domain.IMapElement import *
import copy
import random
import math


class FirstMapStrategy(IMapStrategy):

    def __init__(self):
        pass

    def disposeDestrObstacles(self, map: Map, dstrobstacles: list) -> Map:
        #TODO
        pass

    def disposeUndestrObstacles(self, map: Map, undstrobstacles: list):
        """
        Dispose undestructible obstacles inside a map

        :param map: map where the obstacles must be placed
        :param undstrobstacles: list of different sample of undestructible obstacles that must be placed
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
                        newundstr.setPosition(Position(i,j))
                        undstrarray.append(newundstr)

        map.setUndstrObstacleArray(undstrarray)
        #TODO TEST

    def disposeBoBs(self, map: Map, bobs: list):

        bobtoplace = len(bobs)

        if bobtoplace > 0:
            width = map.getDimensions().getWidth()
            height = map.getDimensions().getHeight()

            bobindex = 0

            maxdim = max(height,width)
            mindim = min(height,width)

            if maxdim == height:
                delta = math.floor(mindim / math.floor(bobtoplace/4))
                for i in range(1,mindim,delta):
                    bobs[bobindex].setPosition(Position(i,1))
                    map.occupyPosition(bobs[bobindex])
                    bobtoplace = bobtoplace - 1
                    bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(maxdim / math.ceil(bobtoplace/3))
                    for i in range(1, maxdim, delta):
                        bobs[bobindex].setPosition(Position(mindim,i))
                        map.occupyPosition(bobs[bobindex])
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(mindim / math.floor(bobtoplace/2))
                    for i in range(mindim, 1, -delta):
                        bobs[bobindex].setPosition(Position(i,maxdim))
                        map.occupyPosition(bobs[bobindex])
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(maxdim / bobtoplace)
                    for i in range(maxdim, 1, -delta):
                        bobs[bobindex].setPosition(Position(1,i))
                        map.occupyPosition(bobs[bobindex])
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1
            else:

                delta = math.floor(mindim / math.floor(bobtoplace / 4))
                for i in range(1, mindim, delta):
                    bobs[bobindex].setPosition(Position(maxdim, i))
                    map.occupyPosition(bobs[bobindex])
                    bobtoplace = bobtoplace - 1
                    bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(maxdim / math.ceil(bobtoplace / 3))
                    for i in range(maxdim, 1, -delta):
                        bobs[bobindex].setPosition(Position(i, mindim))
                        map.occupyPosition(bobs[bobindex])
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(mindim / math.floor(bobtoplace / 2))
                    for i in range(mindim, 1, -delta):
                        bobs[bobindex].setPosition(Position(1, i))
                        map.occupyPosition(bobs[bobindex])
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(maxdim / bobtoplace)
                    for i in range(1, maxdim, delta):
                        bobs[bobindex].setPosition(Position(i, 1))
                        map.occupyPosition(bobs[bobindex])
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1




    def disposePowerUps(self, map: Map, powerups: list) -> Map:
        #TODO
        pass

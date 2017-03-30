from src.utility.mapstrategy import IMapStrategy
from src.utility import Dimensions, Position
from src.model.domain import IMapElement
import copy
import random
import math


class FirstMapStrategy(IMapStrategy):

    def __init__(self):
        pass

    def disposeUndestrObstacles(self, undstrobstacles: list, dim: Dimensions) -> list:
        """
        Dispose undestructible obstacles inside a map

        :param undstrobstacles: list of different sample of undestructible obstacles that must be placed
        :param dim: dimensions of the map to be filled
        """

        height = dim.getHeight()
        width = dim.getWidth()

        undestractibleelementslist = list()

        for i in range(1, height):
            if i%2 == 0:
                for j in range(1, width):
                    if j%2 == 0:
                        newundstr = copy.deepcopy(random.choice(undstrobstacles))
                        newundstr.setPosition(Position(i, j))
                        undestractibleelementslist.append(newundstr)

        return undestractibleelementslist

    def disposeBoBs(self, bobs: list, dim: Dimensions) -> list:

        bobtoplace = len(bobs)

        if bobtoplace > 0:
            width = dim.getWidth()
            height = dim.getHeight()

            bobindex = 0

            maxdim = max(height, width)
            mindim = min(height, width)
            
            newplacedbobs = list()

            tmpbob = None  # temporary variable

            if maxdim == height:
                delta = int(math.floor(mindim / math.floor(bobtoplace/4)))
                for i in range(1, mindim, delta):
                    tmpbob = bobs[bobindex]
                    tmpbob.setPosition(Position(i, 1))
                    newplacedbobs.append(tmpbob)
                    bobtoplace = bobtoplace - 1
                    bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = int(math.floor(maxdim / math.ceil(bobtoplace/3)))
                    for i in range(1, maxdim, delta):
                        tmpbob = bobs[bobindex]
                        tmpbob.setPosition(Position(mindim, i))
                        newplacedbobs.append(tmpbob)
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = int(math.floor(mindim / math.floor(bobtoplace/2)))
                    for i in range(mindim, 1, -delta):
                        tmpbob = bobs[bobindex]
                        tmpbob.setPosition(Position(i, maxdim))
                        newplacedbobs.append(tmpbob)
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = int(math.floor(maxdim / bobtoplace))
                    for i in range(maxdim, 1, -delta):
                        tmpbob = bobs[bobindex]
                        tmpbob.setPosition(Position(1, i))
                        newplacedbobs.append(tmpbob)
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1
            else:

                delta = math.floor(mindim / math.floor(bobtoplace / 4))
                for i in range(1, mindim, delta):
                    tmpbob = bobs[bobindex]
                    tmpbob.setPosition(Position(maxdim, i))
                    newplacedbobs.append(tmpbob)
                    bobtoplace = bobtoplace - 1
                    bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(maxdim / math.ceil(bobtoplace / 3))
                    for i in range(maxdim, 1, -delta):
                        tmpbob = bobs[bobindex]
                        tmpbob.setPosition(Position(i, mindim))
                        newplacedbobs.append(tmpbob)
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(mindim / math.floor(bobtoplace / 2))
                    for i in range(mindim, 1, -delta):
                        tmpbob = bobs[bobindex]
                        bobs[bobindex].setPosition(Position(1, i))
                        newplacedbobs.append(tmpbob)
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

                if bobtoplace > 0:
                    delta = math.floor(maxdim / bobtoplace)
                    for i in range(1, maxdim, delta):
                        tmpbob = bobs[bobindex]
                        tmpbob.setPosition(Position(i, 1))
                        newplacedbobs.append(tmpbob)
                        bobtoplace = bobtoplace - 1
                        bobindex = bobindex + 1

            return newplacedbobs

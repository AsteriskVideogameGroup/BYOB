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

    def disposeBoBs(self, bobs: list, dim: Dimensions):

        bobtoplace = len(bobs)

        if bobtoplace > 0:
            width = dim.getWidth()
            height = dim.getHeight()

            bobindex = 0

            maxdim = max(height, width)

            if maxdim == height:
                bobtoplace, bobindex = self._disposeBoBsOnWidth(1, False, 4, bobtoplace, bobs, bobindex,
                                                                width, False)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnHeight(width, False, 3, bobtoplace, bobs, bobindex,
                                                                     height, True)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnWidth(height, True, 2, bobtoplace, bobs, bobindex,
                                                                    width, False)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnHeight(1, True, 1, bobtoplace, bobs, bobindex,
                                                                     height, True)
            else:

                bobtoplace, bobindex = self._disposeBoBsOnHeight(width, False, 4, bobtoplace, bobs, bobindex,
                                                                 height, False)
                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnWidth(height, True, 3, bobtoplace, bobs, bobindex,
                                                                    width, True)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnHeight(1, True, 2, bobtoplace, bobs, bobindex,
                                                                     height, False)

                if bobtoplace > 0:
                    bobtoplace, bobindex = self._disposeBoBsOnWidth(1, False, 1, bobtoplace, bobs, bobindex,
                                                                    width, True)

    def _disposeBoBsOnHeight(self, x: int, negative: bool, remainingsides: int, remainingbobs: int, bobslist: list,
                             bobit: int, height: int, longside: bool):
        if longside:
            delta = math.floor(height / math.ceil(remainingbobs / remainingsides))
        else:
            delta = math.floor(height / math.floor(remainingbobs / remainingsides))
        if negative:
            for i in range(height, 1, -delta):
                bobslist[bobit].setPosition(Position(x, i))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1
        else:
            for i in range(1, height, delta):
                bobslist[bobit].setPosition(Position(x, i))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1

        return remainingbobs, bobit

    def _disposeBoBsOnWidth(self, y: int, negative: bool, remainingsides: int, remainingbobs: int, bobslist: list,
                            bobit: int, width: int, longside: bool):
        if longside:
            delta = math.floor(width / math.ceil(remainingbobs / remainingsides))
        else:
            delta = math.floor(width / math.floor(remainingbobs / remainingsides))
        if negative:
            for i in range(width, 1, -delta):
                bobslist[bobit].setPosition(Position(i, y))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1
        else:
            for i in range(1, width, delta):
                bobslist[bobit].setPosition(Position(i, y))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1

        return remainingbobs, bobit

    def disposeDestrObstacles(self, dstrobstacles: list, dim: Dimensions) -> list:
        #TODO
        pass


    def disposePowerUps(self, powerups: list, dim: Dimensions) -> list:
        #TODO
        pass

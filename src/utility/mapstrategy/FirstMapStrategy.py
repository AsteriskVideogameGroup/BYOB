from .IMapStrategy import IMapStrategy
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
        :return: list of undestructible obstacles that are positioned
        """

        height = dim.getHeight()
        width = dim.getWidth()

        undestructibleelementslist = list()

        for i in range(1, height):
            if i%2 == 0:
                for j in range(1, width):
                    if j%2 == 0:
                        newundstr = copy.deepcopy(random.choice(undstrobstacles))
                        newundstr.setPosition(Position(i, j))
                        undestructibleelementslist.append(newundstr)

        return undestructibleelementslist

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

    def disposeDestrObstacles(self, dstrobstacles: list, dim: Dimensions, bobs: list) -> list:
        # TODO: test

        """
        Dispose undestructible obstacles inside a map

        :param undstrobstacles: list of different samples of destructible obstacles that must be placed
        :param dim: dimensions of the map to be filled
        :param bobs: list of bobs from which is computed the safe area (obstacles cannot be in safe area)
        :return: list of destructible obstacles that are positioned
        """

        MINDIST = 1                         # Minimum distance from bobs
        PLACINGPROBABILITY = 0.33           # Probability of placing obstacle in a given position

        destructibleelementslist = list()

        safearea = self._selectSafeArea(dim,bobs,MINDIST)

        for y in range(1,dim.getHeight()):
            for x in range(1,dim.getWidth()):
                if not ((x % 2 == 0) and (y % 2 == 0)): # if the position is not (even,even) resume

                    newposition = Position(x,y)
                    if not (newposition.toString() in safearea): # if the position is not in the safearea
                        if random.random() < PLACINGPROBABILITY:

                            newobstacle = copy.deepcopy(random.choice(dstrobstacles))
                            newobstacle.setPosition(newposition)

                            destructibleelementslist.append(newobstacle)

        return destructibleelementslist

    def _selectSafeArea(self, dim: Dimensions, bobs: list, mindist: int) -> list:
        """
        Select area that must be free near bobs
        :param dim: dimensions of the map where to select the safe area
        :param bobs: bob array from which is computed the safe area
        :param mindist: minimum distance that must be free (x and y)
        :return: list of positions that must be left free
        """

        safearea = list()

        for bob in bobs:

            bobx = bob.getPosition().getX()
            boby = bob.getPosition().getY()

            startx = bobx - mindist
            starty = boby - mindist
            endx = bobx + mindist
            endy = boby + mindist

            if startx <= 0:
                startx = 1
            if starty <= 0:
                starty = 1
            if endx > dim.getWidth():
                endx = dim.getWidth()
            if endy > dim.getHeight():
                endy = dim.getHeight()

            for x in range(startx,endx):
                for y in range(starty, endy):
                    if not ((x % 2 == 0) and (y % 2 == 0)):  # if the position is not (even,even) resume
                        safearea.append(Position(x,y).toString())

        return safearea

    def disposePowerUps(self, powerups: list, dim: Dimensions) -> list:
        #TODO
        pass

import copy
import math
import random

from src.utility.metaclasses.MetaSingleton import MetaSingleton

from src.utility.geometrictools import Position
from src.utility.mapstrategy.IMapStrategy import IMapStrategy


class FirstMapStrategy(IMapStrategy, metaclass=MetaSingleton):
    def disposeUndestrObstacles(self, undstrobstacles: list, dim) -> list:
        """
        Dispose undestructible obstacles inside a map in (2k,2k) positions

        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+
        |   | X |   | X |   | X |   | X |   |
        +---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+

        X = undstrobstacles placed        
        :param undstrobstacles: list of different sample of undestructible obstacles that must be placed
        :param dim: dimensions of the map to be filled
        :return: list of undestructible obstacles that are positioned
        """

        height = dim.getHeight()
        width = dim.getWidth()

        undestructibleelementslist = list()

        for i in range(1, height + 1):
            if i % 2 == 0:
                for j in range(1, width + 1):
                    if j % 2 == 0:
                        newundstr = copy.deepcopy(random.choice(undstrobstacles))
                        newundstr.setPosition(Position(i, j))
                        undestructibleelementslist.append(newundstr)

        return undestructibleelementslist

    def disposeBoBs(self, bobs: list, dim):
        """
        Disposal algorithm for BoBs (balanced number of BoBs for each side: longer side => more BoBs)

        examples: 6 BoBs on 7x5 map

         +---+---+---+---+---+---+---+
         | X |   |   | X |   |   | X |
         +---+---+---+---+---+---+---+
         |   |   |   |   |   |   |   |
         +---+---+---+---+---+---+---+
         |   |   |   |   |   |   |   |
         +---+---+---+---+---+---+---+
         |   |   |   |   |   |   |   |
         +---+---+---+---+---+---+---+
         | X |   |   | X |   |   | X |
         +---+---+---+---+---+---+---+

         X = BoB placed 

        :param bobs: BoBs that must be placed
        :param dim: Map dimensions
        """

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
        """
        Subroutine for the disposal of BoBs in a column of the map
        :param x: number of the column
        :param negative: true, if the disposal starts from the end of the column, or false, if the disposal starts from the beginning of the column
        :param remainingsides: number of other columns or rows where bobs have to be disposed
        :param remainingbobs: number of remaining disposing bobs
        :param bobslist: list of disposing bobs
        :param bobit: index of bobslist from which must be dispose the bobs
        :param height: height of the column
        :param longside: true, if the columns are longer than rows, or false, otherwise
        :return: the number of remaining disposing bobs and the index of bobs array from which resume the disposing
        """
        if longside:
            delta = math.floor(height / math.ceil(remainingbobs / remainingsides))
        else:
            delta = math.floor(height / math.floor(remainingbobs / remainingsides))
        if negative:
            for i in range(height, 1 + 1, -delta):
                bobslist[bobit].setPosition(Position(x, i))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1
        else:
            for i in range(1, height + 1, delta):
                bobslist[bobit].setPosition(Position(x, i))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1

        return remainingbobs, bobit

    def _disposeBoBsOnWidth(self, y: int, negative: bool, remainingsides: int, remainingbobs: int, bobslist: list,
                            bobit: int, width: int, longside: bool):
        """
        Subroutine for the disposal of BoBs in a row of the map
        :param y: number of the row
        :param negative: true, if the disposal starts from the end of the row, or false, if the disposal starts from the beginning of the row
        :param remainingsides: number of other columns or rows where bobs have to be disposed
        :param remainingbobs: number of remaining disposing bobs
        :param bobslist: list of disposing bobs
        :param bobit: index of bobslist from which must be dispose the bobs
        :param width: width of the row
        :param longside: true, if the rows are longer than columns, or false, otherwise
        :return: the number of remaining disposing bobs and the index of bobs array from which resume the disposing
        """

        if longside:
            delta = math.floor(width / math.ceil(remainingbobs / remainingsides))
        else:
            delta = math.floor(width / math.floor(remainingbobs / remainingsides))
        if negative:
            for i in range(width, 1 + 1, -delta):
                bobslist[bobit].setPosition(Position(i, y))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1
        else:
            for i in range(1, width + 1, delta):
                bobslist[bobit].setPosition(Position(i, y))
                remainingbobs = remainingbobs - 1
                bobit = bobit + 1

        return remainingbobs, bobit

    def disposeDestrObstacles(self, dstrobstacles: list, dim, bobs: list) -> list:
        """
        Randomly dispose destructible obstacles inside a map (caring about a safe zone near BoBs)

        example: 4 BoBs on 7x7 map. (safe zone of 1 tile)

        +---+---+---+---+---+---+---+
        | $ | + | X |   |   | + | $ |
        +---+---+---+---+---+---+---+
        | + | # | X | # |   | # | + |
        +---+---+---+---+---+---+---+
        |   |   |   | X |   | X |   |
        +---+---+---+---+---+---+---+
        |   | # | X | # |   | # |   |
        +---+---+---+---+---+---+---+
        |   | X | X | X |   |   |   |
        +---+---+---+---+---+---+---+
        | + | # | X | # |   | # | + |
        +---+---+---+---+---+---+---+
        | $ | + |   |   |   | + | $ |
        +---+---+---+---+---+---+---+

        # = Undestructible obstacles
        X = Destructible obstacles
        + = Safe zone
        $ = BoB

        :param undstrobstacles: list of different samples of destructible obstacles that must be placed
        :param dim: dimensions of the map to be filled
        :param bobs: list of bobs from which is computed the safe area (obstacles cannot be in safe area)
        :return: list of destructible obstacles that are positioned
        """

        MINDIST = 1  # Minimum distance from bobs
        PLACINGPROBABILITY = 0.45  # Probability of placing obstacle in a given position

        destructibleelementslist = list()

        safearea = self._selectSafeArea(dim, bobs, MINDIST)

        for y in range(1, dim.getHeight() + 1):
            for x in range(1, dim.getWidth() + 1):
                if not ((x % 2 == 0) and (y % 2 == 0)):  # if the position is not (even,even) resume

                    newposition = Position(x, y)
                    if not (newposition in safearea):  # if the position is not in the safearea
                        if random.random() < PLACINGPROBABILITY:
                            newobstacle = copy.deepcopy(random.choice(dstrobstacles))
                            newobstacle.setPosition(newposition)

                            destructibleelementslist.append(newobstacle)

        return destructibleelementslist

    def _selectSafeArea(self, dim, bobs: list, mindist: int) -> list:
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

            if startx < 1:
                startx = 1
            if starty < 1:
                starty = 1
            if endx > dim.getWidth():
                endx = dim.getWidth()
            if endy > dim.getHeight():
                endy = dim.getHeight()

            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    if not ((x % 2 == 0) and (y % 2 == 0)):  # if the position is not (even,even) resume
                        safearea.append(Position(x, y))

        return safearea

    def disposePowerUps(self, powerups: list, dim, occpositions: dict) -> list:
        """
        Randomly place a list of power-ups on the map (in an unoccupied position)
        :param powerups: list of power-ups to place
        :param dim: dimension of the map where to place the power-ups
        :param occpositions: dictionary with Position as keys to sign the occupied positions
        :return: list of placed power-ups
        """

        poweruplist = list()
        for pu in powerups:
            newy = random.randrange(1, dim.getHeight() + 1)
            newx = random.randrange(1, dim.getWidth() + 1)
            newpos = Position(newx, newy)
            ## TODO: Potrebbe dare problemi quando si andrà a rendere fluido il movimento dei BoB
            ## TODO: Essi potranno trovarsi nel punto di spawn del power-up se la loro posizione è float e non int
            while (newpos in occpositions):
                newy = random.randrange(1, dim.getHeight() + 1)
                newx = random.randrange(1, dim.getWidth() + 1)
                newpos = Position(newx, newy)

            pu.setPosition(newpos)
            poweruplist.append(pu)

        return poweruplist
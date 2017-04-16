class Position:

    ########## ATTRIBUTES DEFINITION ##########

    # _x : float
    # _y : float

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other):
        return (self._x, self._y) == (other._x, other._y)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def setX(self, x: float):
        self._x = x

    def setY(self, y: float):
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def toString(self):
        """
        :return: the position as: (_x,_y)
        """
        return "("+str(self._x)+","+str(self._y)+")"


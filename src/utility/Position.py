class Position:

    _x = None
    _y = None

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def setX(self, x: float):
        self._x = x

    def setY(self, y: float):
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def toString(self):
        return "("+str(self._x)+","+str(self._y)+")"
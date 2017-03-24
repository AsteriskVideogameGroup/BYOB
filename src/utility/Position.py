class Position:

    _x = None
    _y = None

    def __init__(self):
        self._x = 0
        self._y = 0

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
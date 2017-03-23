class Dimensions:

    _width = None
    _height = None

    def __init__(self):
        self._width = 0
        self._y = 0

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def setX(self, width: int):
        self._width = width

    def setY(self, height: int):
        self._height = height
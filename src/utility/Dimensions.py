class Dimensions:

    _width = None
    _height = None

    def __init__(self):
        self._width = 0
        self._height = 0

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def setWidth(self, width: int):
        self._width = width

    def setHeight(self, height: int):
        self._height = height

    def getHeight(self):
        return self._height

    def getWidth(self):
        return self._width
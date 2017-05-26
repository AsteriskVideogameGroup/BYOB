from src.foundation.metaclasses.MetaSingleton import MetaSingleton


class GameHandlerProxyWrapperSingleton(metaclass=MetaSingleton):

    def __init__(self):
        self._gamehandlerproxy = None

    def setGameHandler(self, ghandler):
        self._gamehandlerproxy = ghandler

    def getMap(self):
        if self._gamehandlerproxy is None:
            raise EnvironmentError('SERVICE: GameHandler not set yet')
        return self._gamehandlerproxy.getMap()
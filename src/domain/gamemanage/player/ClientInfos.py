class ClientInfos:
    def __init__(self, player):
        self._player = player
        self._gamehandler = None

    def update(self, newghandle):
        self._gamehandler = newghandle

    def getPlayer(self):
        return self._player
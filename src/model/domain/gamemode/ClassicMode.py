from src.model.domain.gamemode.IGameMode import IGameMode


class ClassicMode(IGameMode):

    def __init__(self):
        self._maxplayer = 4

    def __str__(self):
        return "classico"

    def getMaxPlayers(self):
        return self._maxplayer
from src.model.domain.gamemode.IGameMode import IGameMode


class DifferentMode(IGameMode):

    def __init__(self):
        self._maxplayer = 7

    def __str__(self):
        return "diff"

    def getMaxPlayers(self):
        return self._maxplayer
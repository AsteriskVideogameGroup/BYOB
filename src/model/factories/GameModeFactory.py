from src.model.domain.gamemode.IGameMode import *


class GameModeFactory:
    class _Implementation:
        def __init__(self):
            pass

        def getGameMode(modeid: str) -> IGameMode:
            """ Translate modeid to the proper IGameMode """

            # TODO
            pass

    _instance = None  # singleton instance

    def __init__(self):
        raise SyntaxError  # throw exception

    @classmethod
    def getInstance(cls) -> _Implementation:
        if not cls._instance:
            cls._instance = cls._Implementation()

        return cls._instance

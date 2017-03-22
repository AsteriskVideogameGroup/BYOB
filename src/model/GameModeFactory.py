from src.model.IGameMode import *


class GameModeFactory:
    class __Implementation:
        def __init__(self):
            pass

        def getGameMode(modeid: str) -> IGameMode:
            """ Translate modeid to the proper IGameMode """

            # TODO
            pass

    _instance: __Implementation = None  # singleton instance

    def __init__(self):
        raise SyntaxError  # throw exception

    @classmethod
    def getInstance(cls) -> __Implementation:
        if not cls._instance:
            cls._instance = cls.__Implementation()

        return cls._instance

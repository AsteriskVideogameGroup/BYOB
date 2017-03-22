from typing import Dict
from src.model.GameMode import *

class MatchMaker:

    _modes: Dict[str, GameMode] = Dict[str, GameMode]  # singleton instance

    def __init__(self):
        raise SyntaxError  # throw exception

    @classmethod
    def getInstance(cls, gamemode: str) -> GameMode:
        """
        Gives an instance of the matchmaker suitable for the selected GameMode

        :param gamemode: String ID of the GameMode
        :return: The selected GameMode
        """
        if not gamemode in MatchMaker._modes:
            cls._translateModeID(gamemode)

        return cls._modes.get(gamemode)

    @classmethod
    def _translateModeID(cls, gamemode: str):

        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes

        :param gamemode: String ID of the GameMode
        """
        pass  # TODO

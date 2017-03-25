from src.model.domain.Player import Player


class Room:

    _arrplayers = None

    def __init__(self):
        self._arrplayers = list() # list of the gamers

    def addPlayer(self, player: Player):
        """
        Add a player to the Room
        :param player: Player to be add
        """
        self._arrplayers.append(player)

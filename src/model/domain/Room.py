from src.model.domain.Player import Player


class Room:

    _arrplayers = None

    def __init__(self):
        pass

    def addPlayer(self, player: Player):
        self._arrplayers.append(player)


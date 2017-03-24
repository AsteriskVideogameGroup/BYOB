from src.model.domain.Player import Player


class ClientInfos:
    def __init__(self, player: Player):
        self._player = player

    def update(self):
        print("sono stato scelto")
        # TODO
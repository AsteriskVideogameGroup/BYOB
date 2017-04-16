from src.domain.gamemanage.player import Player


class ClientInfos:
    def __init__(self, player: Player):
        self.player = player

    def update(self, newghandle): # TODO newghandle: GameHandler
        print("sono stato scelto")
        # TODO
from src.model.domain.Player import Player
#from src.control.GameHandler import GameHandler


class ClientInfos:
    def __init__(self, player: Player):
        self.player = player

    def update(self, newghandle): # TODO newghandle: GameHandler
        print("sono stato scelto")
        # TODO
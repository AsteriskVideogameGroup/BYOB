class Player:
    def __init__(self):
        pass


class Room:
    ########## ATTRIBUTES DEFINITION ##########

    # _arrplayers : list (of Player)

    def __init__(self):
        self._arrplayers = list()  # list of the gamers

    def addPlayer(self, player: Player):
        """
        Add a player to the Room
        :param player: Player to be add
        """
        self._arrplayers.append(player)


class ClientInfos:
    def __init__(self, player: Player):
        self.player = player

    def update(self, newghandle):  # TODO newghandle: GameHandler
        print("sono stato scelto")
        # TODO

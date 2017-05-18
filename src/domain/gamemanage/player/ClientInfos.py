import Pyro4

from src.utility.netmiddleware.NetworkObjectTranslator import NetworkObjectTranslator
from src.control.gamemanage.GameHandler import GameHandler


@Pyro4.expose
class ClientInfos:
    def __init__(self, player):
        self._player = player
        self._gamehandler = None

    def update(self, state: dict):
        print(state)  # TODO da fargli fare qualcosa

    def notifyGameHandler(self, gamehandlername: str):
        proxygamehandler = NetworkObjectTranslator().translate(gamehandlername)
        self._gamehandler = proxygamehandler

    def getPlayer(self):
        return self._player

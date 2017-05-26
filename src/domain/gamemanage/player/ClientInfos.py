import Pyro4

from src.control.clientgamemanage.GameHandlerProxyWrapperSingleton import GameHandlerProxyWrapperSingleton
from src.domain.client_gamemanage.gameessentials.ClientGameSingleton import ClientGameSingleton
from src.foundation.netmiddleware.NetworkObjectTranslator import NetworkObjectTranslator
from src.domain.gamemanage.gameessentials.Map import Map # per il clone della mappa


@Pyro4.expose
class ClientInfos:
    def __init__(self, player):
        self._player = player

    def update(self, state: dict):
        if state["map-ready"] is not None:  # TODO modificare, non mi piace questo tipo di controllo
            #  dict contenga sempre tutti i flag e poi venga controllato solo quale è true
            mapclone = GameHandlerProxyWrapperSingleton().getMap()
            ClientGameSingleton().setMap(mapclone)

    def notifyGameHandler(self, gamehandlername: str):
        proxygamehandler = NetworkObjectTranslator().translate(gamehandlername)
        GameHandlerProxyWrapperSingleton().setGameHandler(proxygamehandler)

    def getPlayer(self):
        return self._player

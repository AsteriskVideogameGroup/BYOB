class ClientInfos:
    def __init__(self, player: 'src.domain.gamemanage.player.Player'):
        self._player = player
        self._gamehandler = None

    def update(self, newghandle : 'src.control.gamemanage.GameHandler'):
        self._gamehandler = newghandle

import src.control.gamemanage.GameHandler
import src.domain.gamemanage.player.Player
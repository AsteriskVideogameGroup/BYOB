import threading
import time
import uuid

import Pyro4

from src.domain.gamemanage.bob.BoBBuilder import BoBBuilder
from src.foundation.settings.GlobalSettings import GlobalSettings


@Pyro4.expose
class GameHandler:
    CHOOSEBOBCOUNTDOWN = "choosebobcountdown"

    ########## ATTRIBUTES DEFINITION ##########
    # _currentgame : Game
    # _started : Bool
    # _bobselectable: Bool

    def __init__(self, newgame, clients: list):
        """
        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._clientslist = clients
        self._uniquename = str(uuid.uuid4())

        # stato della partita
        self._gamestarted = False
        self._bobselectable = True
        self._mapready = False

    def getUniqueName(self):
        return self._uniquename

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._gamestarted = self._currentgame.startGame()

    def chooseBoB(self, owner, bobnameid: str = 'random'):
        """
        Let the player choose his BoB
        :param owner: Player who choose the BoB
        :param bobnameid: Name id of the chosen BoB
        """
        if self._bobselectable:
            newbob = BoBBuilder().createBoB(bobnameid, owner)
            self._currentgame.addBoB(newbob)

    def startBoBSelectionCountdown(self):
        self._startDaemon(self._BoBSelectionDaemon)

    def _startDaemon(self, target):
        newthread = threading.Thread(target=target, args=())
        newthread.start()

    def _BoBSelectionDaemon(self):

        timemax = GlobalSettings().getSetting(GameHandler.CHOOSEBOBCOUNTDOWN)

        timewaited = 0

        numplayers = self._currentgame.getRoom().getNumPlayers()

        while timewaited < timemax and len(self._currentgame.getBoBArray()) < numplayers:
            time.sleep(0.1)
            timewaited += 0.1

        bobarray = self._currentgame.getBoBArray()

        for client in self._clientslist:
            choose = False
            for bob in bobarray:
                print("debug 2")
                if client.getPlayer() == bob.getOwner():
                    choose = True
                    break
            if not choose:
                self.chooseBoB(client.getPlayer())

        print("debug3")

        self._bobselectable = False  # flag: Bobs are no more selectable
        self._mapready = True  # flag: the Map is ready to print

        self.prepareGame()  # TODO DA DISCUTERE

        for client in self._clientslist:
            client.update({"map-ready": self._mapready})

    def isBoBSelectable(self):
        return self._bobselectable

    def isMapReady(self):
        return self._mapready

    def isGameStarted(self):
        return self._gamestarted

    def getMap(self):
        return self._currentgame.getMap()

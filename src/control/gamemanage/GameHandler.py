import threading
import time

class GameHandler:

    CHOOSEBOBCOUNTDOWN = "choosebobcountdown"

    ########## ATTRIBUTES DEFINITION ##########
    # _currentgame : Game
    # _started : Bool
    # _bobselectable: Bool

    def __init__(self, newgame: 'src.domain.gamemanage.gameessentials.Game', clients: list):
        """
        :param newgame: Game object to handle
        """
        self._currentgame = newgame
        self._started = False
        self._bobselectable = False
        self._clientslist = clients

    def prepareGame(self):
        """ Prepare the game for the start"""

        self._currentgame.prepareGame()
        self._started = self._currentgame.startGame()

    def chooseBoB(self, owner: 'src.domain.gamemanage.player.Player', bobnameid: str = 'random'):
        """
        Let the player choose his BoB
        :param owner: Player who choose the BoB
        :param bobnameid: Name id of the chosen BoB
        """
        if self._bobselectable:
            import src.domain.gamemanage.bob.BoBBuilder as BoBBuilder

            newbob = BoBBuilder().createBoB(bobnameid, owner)
            self._currentgame.addBoB(newbob)

    def BoBSelectionCountdownStart(self):
        self._startDaemon(self._BoBSelectionDaemon)

    def _startDaemon(self, target):
        newthread = threading.Thread(target=target,args=())
        newthread.start()

    def _BoBSelectionDaemon(self):
        import src.utility.settings.GlobalSettings as GlobalSettings

        timemax = GlobalSettings().getSetting(GameHandler.CHOOSEBOBCOUNTDOWN)

        timewaited = 0

        self._bobselectable = True
        numplayers = self._currentgame.getRoom().getNumPlayers()

        while timewaited < timemax and len(self._currentgame.getBoBArray()) < numplayers:
            time.sleep(0.1)
            timewaited += 0.1


        bobarray = self._currentgame.getBoBArray()

        for client in self._clientslist:
            choose = False
            for bob in bobarray:
                if client.getPlayer() == bob.getOwner():
                    choose = True
                    break
            if not choose:
                self.chooseBoB(client.getPlayer())

        self._bobselectable = False

        self.prepareGame()    #TODO DA DISCUTERE

        for client in self._clientslist:
            client.update(self)




import src.domain.gamemanage.bob.BoB
import src.domain.gamemanage.gameessentials.Game
import src.domain.gamemanage.player.Player

import serpent

from src.control.gamemanage.GameHandler import GameHandler
from src.domain.gamemanage.gameessentials.Game import Game
from src.domain.gamemanage.gamemode.ModeBuilder import ModeBuilder
from src.domain.gamemanage.player.Room import Room
from src.domain.gamemanage.player.Player import Player


class MatchMaker:

    _modes = dict()  # singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._modes.get(args[0], None) is None:

            mode = ModeBuilder().getMode(args[0]) # translate gamemode ID to IGameMode
            newmatchmaker = super().__new__(cls)  # instantiate new Matchmaker
            newmatchmaker._mode = mode  # assign a mode to the matchmaker
            newmatchmaker._unrankedqueue = list()
            newmatchmaker._rankedqueue = list()
            cls._modes[args[0]] = newmatchmaker  # add newmatchmaker into the dict

        return cls._modes.get(args[0])

    @classmethod
    def getInstance(cls, gamemode: str):
        """
        Gives an instance of the matchmaker suitable for the selected GameMode
        :param gamemode: String ID of the GameMode
        :return: The selected matchmaker for the GameMode
        """
        return cls.__new__(cls(), gamemode)

    def pushPlayer(self, client, isranked: bool):
        """
        Add a Client to the list of the availables
        :param client: Client of the Player who wants to join a game
        :param isranked: Specifies if the Game is ranked
        """
        if isranked is True:
            # TODO non facciamo le ranked
            self._rankedqueue.append(client)
            self._rankedqueue.sort()
            # TODO controllare associazione giocatori
        else:
            self._unrankedqueue.append(client)  # add client to the list
            self._extractClients(self._unrankedqueue)

    def _extractClients(self, queue: list):
        maxplayer = self._mode.getMaxPlayers()  # maxplayers depends on the GameMode
        if len(queue) >= maxplayer:

            print("Room pronta con " + str(len(queue)) + " gioacatori")  # TODO log rimuovi

            playerroom = Room()  # bundle of player that will play
            arrclients = list()  # list of the selected players


            for i in range(0, maxplayer):
                client = queue.pop(0)

                # TODO migliorare

                #player_ser:dict = client.getPlayer()
                #palyer = serpent.loads(player_ser.encode())

                #print(player_ser)
                playerroom.addPlayer(client.getPlayer())
                arrclients.append(client)

            print(arrclients)
            
            newgame = Game(playerroom, self._mode)  # instantiate the new game
            ghandle = GameHandler(newgame, arrclients)  # creates the new controller for the clients

            # TODO implementare update
            #for client in arrclients:  # update all client observers
                #client.update(ghandle)

            print("debug")

            ghandle.BoBSelectionCountdownStart()


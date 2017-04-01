from typing import List
from src.control.GameHandler import GameHandler # TODO correggere
from src.model.domain import ClientInfos
from src.model.factories import GameModeFactory
from .Room import Room
from .Game import Game


class MatchMaker:

    _modes = dict()  # singleton instance

    def __new__(cls, *args, **kwargs) -> 'MatchMaker':
        if cls._modes.get(args[0], None) is None:
            mode = GameModeFactory().getGameMode(args[0])  # translate gamemode ID to IGameMode
            newmatchmaker = super().__new__(cls)  # instantiate new Matchmaker
            newmatchmaker._mode = mode  # assign a mode to the matchmaker
            newmatchmaker._unrankedqueue = list()
            newmatchmaker._rankedqueue = list()
            cls._modes[args[0]] = newmatchmaker  # add newmatchmaker into the dict

        return cls._modes.get(args[0])

    @classmethod
    def getInstance(cls, gamemode: str) -> 'MatchMaker':
        """
        Gives an instance of the matchmaker suitable for the selected GameMode
        :param gamemode: String ID of the GameMode
        :return: The selected matchmaker for the GameMode
        """
        return cls.__new__(cls(), gamemode)

    def pushPlayer(self, client: ClientInfos, isranked: bool):
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

    def _extractClients(self, queue: List[ClientInfos]):
        maxplayer = self._mode.getMaxPlayers()  # maxplayers depends on the GameMode
        if len(queue) >= maxplayer:

            print("Room pronta con " + str(len(queue)) + " gioacatori")  # TODO rimuovi

            playerroom = Room()  # bundle of player that will play
            arrclients = list()  # list of the selected players

            for i in range(0, maxplayer):
                client = queue.pop(0)
                playerroom.addPlayer(client.player)
                arrclients.append(client)

            # TODO da completare quando la Map sarà corretta
            
            newgame = Game(playerroom, self._mode)  # instantiate the new game
            ghandle = GameHandler(newgame)  # creates the new controller for the clients

            for client in arrclients:  # update all client observers
                client.update(ghandle)


        else:
            print("Ho cercato di fare update ")  # TODO rimuovere
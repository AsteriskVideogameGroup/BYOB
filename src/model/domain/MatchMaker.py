from typing import List
from src.model.domain.gamemode.ClassicMode import ClassicMode
from src.utility.ClientInfos import ClientInfos
from src.model.factories.GameModeFactory import GameModeFactory


class MatchMaker:

    _modes = dict()  # singleton instance

    def __new__(cls, *args, **kwargs) -> 'MatchMaker':
        if cls._modes.get(args[0], None) is None:
            mode = GameModeFactory.getInstance().getGameMode(args[0])  # translate gamemode ID to IGameMode
            newmatchmaker: 'MatchMaker' = super().__new__(cls)  # instantiate new Matchmaker
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
        return cls.__new__(cls, gamemode)

    @classmethod
    def _translateModeID(cls, gamemode: str) -> ClassicMode:
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes

        :param gamemode: String ID of the GameMode
        """
        newmodeclass = globals()[gamemode]

        return newmodeclass()

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
        maxplayer = self._mode.maxplayer # maxplayers depends on the GameMode
        if len(queue) >= maxplayer:
            for i in range(0, maxplayer):
                client = queue.pop(0) # prendi sempre il primo
                client.update()
        else:
            print("Ho cercato di fare update")  # TODO rimuovere


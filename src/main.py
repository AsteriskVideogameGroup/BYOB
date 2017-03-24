from src.control.MatchMakingHandler import MatchMakingHandler
from src.model.domain.ClientInfos import ClientInfos
from src.model.domain.MatchMaker import MatchMaker
from src.model.domain.Player import Player

p = Player()
c = ClientInfos(p)

MatchMakingHandler().makeNewGame(c, "ClassicMode", False)
MatchMakingHandler().makeNewGame(c, "ClassicMode", False)
MatchMakingHandler().makeNewGame(c, "DifferentMode", False)
MatchMakingHandler().makeNewGame(c, "ClassicMode", False)

MatchMakingHandler().makeNewGame(c, "DifferentMode", False)
MatchMakingHandler().makeNewGame(c, "ClassicMode", False)


from src.model.domain.MatchMaker import MatchMaker
from src.utility.ClientInfos import ClientInfos
from src.model.domain.Player import Player

x = MatchMaker("ClassicMode")

p = Player()
c = ClientInfos(p)

x.pushPlayer(c, False)
x.pushPlayer(c, False)
x.pushPlayer(c, False)
x.pushPlayer(c, False)
x.pushPlayer(c, False)
x.pushPlayer(c, False)
x.pushPlayer(c, False)
x.pushPlayer(c, False)
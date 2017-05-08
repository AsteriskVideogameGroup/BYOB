# from src.domain.gamemanage.bob import BoBCatalog

# BoBCatalog().getBoBByID("classic")
#from src.domain.gamemanage.gamemode import ModeMultiton
from src.control.gamemanage.MatchMakingHandler import MatchMakingHandler
from src.domain.gamemanage.player.ClientInfos import ClientInfos
from src.domain.gamemanage.player.Player import Player
from src.utility.geometrictools import Dimensions


p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()

c1 = ClientInfos(p1)
c2 = ClientInfos(p2)
c3 = ClientInfos(p3)
c4 = ClientInfos(p4)

MatchMakingHandler().makeNewGame(c1)
MatchMakingHandler().makeNewGame(c2)
MatchMakingHandler().makeNewGame(c3)
MatchMakingHandler().makeNewGame(c4)

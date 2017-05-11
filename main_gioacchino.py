'''
# from src.domain.gamemanage.bob import BoBCatalog

# BoBCatalog().getBoBByID("classic")
from src.domain.gamemanage.bob.BoB import BoB
from src.domain.gamemanage.player.Player import Player


p1 = Player()

b = BoB("descr", p1)

from src.control.gamemanage.MatchMakingHandler import MatchMakingHandler
from src.domain.gamemanage.gamemode.ModeBuilder import ModeBuilder
from src.domain.gamemanage.player.ClientInfos import ClientInfos
from src.domain.gamemanage.player.Player import Player

p1 = Player()
client1 = ClientInfos(p1)
p2 = Player()
client2 = ClientInfos(p2)
p3 = Player()
client3 = ClientInfos(p3)
p4 = Player()
client4 = ClientInfos(p4)
p5 = Player()
client5 = ClientInfos(p5)
p6 = Player()
client6 = ClientInfos(p6)
p7 = Player()
client7 = ClientInfos(p7)
p8 = Player()
client8 = ClientInfos(p8)

MatchMakingHandler().makeNewGame(client1, "classic_debug", False)
MatchMakingHandler().makeNewGame(client2, "classic_debug", False)
MatchMakingHandler().makeNewGame(client3, "classic_debug", False)
MatchMakingHandler().makeNewGame(client4, "classic_debug", False)
MatchMakingHandler().makeNewGame(client5, "classic_debug", False)
MatchMakingHandler().makeNewGame(client6, "classic_debug", False)
MatchMakingHandler().makeNewGame(client7, "classic_debug", False)
MatchMakingHandler().makeNewGame(client8, "classic_debug", False)
'''
from src.domain.gamemanage.player.ClientInfos import ClientInfos
from src.domain.gamemanage.player.Player import Player
from src.utility.netmiddleware.PyroNetMiddlewareAdapter import PyroNetMiddlewareAdapter

md = PyroNetMiddlewareAdapter()
p1 = Player()
client1 = ClientInfos(p1)
md.register(client1, "ciao")
print("rady")
# md.initService()

p7 = Player()
client7 = ClientInfos(p7)
md.register(client7, "ultimoarrivato")
print("oh my god")
md.initService()












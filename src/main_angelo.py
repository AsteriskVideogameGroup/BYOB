import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.control.gamemanage.MatchMakingHandler as MatchMakingHandler
import src.control.gamemanage.GameHandler as GameHandler
import src.domain.gamemanage.player.Player as Player
import src.domain.gamemanage.player.ClientInfos as ClientInfos
import src.domain.gamemanage.player.Room as Room
import src.domain.gamemanage.gameessentials.Game as Game
import src.domain.gamemanage.bob.BoBDescription as BoBDescription
import src.domain.gamemanage.bob.BoB as BoB
import src.domain.gamemanage.gamemode.GameModeFactory as GameModeFactory

room = Room()
p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()

gm = GameModeFactory().getGameMode("classic")
g = Game(room, gm)
gh = GameHandler.GameHandler(g)
d1 = BoBDescription()
d2 = BoBDescription()
d3 = BoBDescription()
d4 = BoBDescription()
b1 = BoB(d1,p1)
b2 = BoB(d2,p2)
b3 = BoB(d3,p3)
b4 = BoB(d4,p4)
g.addBoB(b1)
g.addBoB(b2)
g.addBoB(b3)
g.addBoB(b4)
g.prepareGame()

print("\n ##### BOB POSITION #####\n")

for b in g._bobarray:
    print(b.getPosition().toString())

print("\n ##### DESTRUCTIBLE OBSTACLES POSITION ##### \n")

for dst in g._gamemap._dstrobstaclearray:
    print(dst.getPosition().toString())

print("\n ##### UNDESTRUCTIBLE OBSTACLES POSITION ##### \n")

for undst in g._gamemap._undstrobstaclearray:
    print(undst.getPosition().toString())
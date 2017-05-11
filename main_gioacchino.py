'''
# from src.domain.gamemanage.bob import BoBCatalog

# BoBCatalog().getBoBByID("classic")
from src.domain.gamemanage.bob.BoB import BoB
from src.domain.gamemanage.player.Player import Player


p1 = Player()

b = BoB("descr", p1)
'''
from src.domain.gamemanage.gamemode.ModeBuilder import ModeBuilder

ModeBuilder().build("classic_debug")


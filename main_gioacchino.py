# from src.domain.gamemanage.bob import BoBCatalog

# BoBCatalog().getBoBByID("classic")
from src.domain.gamemanage.gamemode import ModeMultiton
from src.utility.geometrictools import Dimensions

mult: ModeMultiton = ModeMultiton("classic")
dim: Dimensions = mult.getDimensions()

print(dim.getWidth())

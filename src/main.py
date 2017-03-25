from src.utility.mapstrategy.FirstMapStrategy import *
from src.model.domain.BoB import *
from src.utility.Dimensions import *
from src.utility.Position import *
from src.model.domain.obstacle.UndestructibleObstacle import *

m = Map()
m.setDimensions(Dimensions(11,17))
algo = FirstMapStrategy()
b = [UndestructibleObstacle()]
algo.disposeUndestrObstacles(m,b)
for bob in m._undstrobstaclearray:
    print("("+str(bob.getPosition().getX())+","+str(bob.getPosition().getY())+")")
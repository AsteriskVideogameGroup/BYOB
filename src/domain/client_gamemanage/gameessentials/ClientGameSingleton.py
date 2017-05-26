from src.domain.client_gamemanage.gameessentials.GraphicMap import GraphicMap
from src.foundation.metaclasses.MetaSingleton import MetaSingleton


class ClientGameSingleton(metaclass=MetaSingleton):

    def __init__(self):
        self._graphicmap = GraphicMap()  # map to be printed

    def setMap(self, map):
        """
        Bind all logical IMapElement to GraphicalIMapElement
        :param map: logical map with the elements to be binded
        """
        self._graphicmap.setLogicalMap(map)





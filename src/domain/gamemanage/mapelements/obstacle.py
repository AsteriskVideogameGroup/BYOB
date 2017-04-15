import src.domain.gamemanage.mapelements.mapelements as mapelements
import src.utility.geometrictools as geometrictools


class IObstacle(mapelements.IMapElement):  # , metaclass=abc.ABCMeta):
    pass


class UndestructibleObstacle(IObstacle):
    ########## ATTRIBUTES DEFINITION ##########
    # _position : Position

    def getPosition(self) -> geometrictools.Position:
        """
        :return: the position of the obstacle
        """
        return self._position

    def setPosition(self, position: geometrictools.Position):
        """
        Set the position of the obstacle
        :param position: the position to set
        """
        self._position = position


class DestructibleObstacle(IObstacle):
    ########## ATTRIBUTES DEFINITION ##########
    # _position : Position

    def getPosition(self) -> geometrictools.Position:
        """
        :return: the position of the obstacle
        """
        return self._position

    def setPosition(self, position: geometrictools.Position):
        """
        Set the position of the obstacle
        :param position: the position to set
        """
        self._position = position

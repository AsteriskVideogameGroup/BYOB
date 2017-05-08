class Mode:

    ########## ATTRIBUTES DEFINITION ##########
    # _dimensions : Dimensions
    # _environmentobjectfactory : IEnvironmentObjectFactory
    # _maxplayers : Int
    # _invulnerabilitytime : Int
    # _duration : Int
    # _name : String
    # _mapstrategy: IMapStrategy

    def __init__(self, name: str, dimensions, envobjf, positionalgorithm, maxplayers: int, invtime: int, duration: int):
        self._dimensions = dimensions
        self._environmentobjectfactory = envobjf
        self._maxplayers = maxplayers
        self._invulnerabilitytime = invtime
        self._duration = duration
        self._name = name
        self._mapstrategy = positionalgorithm

    def getMapStrategy(self):
        """
        :return: map elements' disposal algorithm object
        """
        return self._mapstrategy

    def getMapDimensions(self):
        """ 
        :return: map's dimensions for a given mode
        """
        return self._dimensions

    def getEnvironmentObjectFactory(self):
        """
        :return: the factory that must produce the environment objects for a given mode
        """
        return self._environmentobjectfactory

    def getInvulnerabilityTime(self) -> int:
        """
        :return: the time of invulnerability for a, just damaged, Player
        """
        return self._invulnerabilitytime

    def getMaxPlayers(self) -> int:
        """
        Get the number of player who can play contemporary in this mode
        :return:
        """
        return self._maxplayers

    def getDuration(self) -> int:
        """
        :return: duration of each game of the same mode, in minutes
        """
        return self._duration



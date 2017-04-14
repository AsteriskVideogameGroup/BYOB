from src.utility import MetaSingleton, GlobalSettings


class StrategyFactory(metaclass=MetaSingleton):

    #TODO CANCELLARE LA CLASSE, LA LETTURA DELLA MAP STRATEGY è nella MODALITÀ


    def getMapStrategy(self):
        """
        Takes, from configuration, the map strategy that must be used
        :return: the map strategy that must be used
        """
        MAPSTRATEGY = 'mapstrategy'
        mapstrategyname = GlobalSettings().getSetting(MAPSTRATEGY)
        mapstrategy = globals()[mapstrategyname]
        self._mapstrategy = mapstrategy
        return self._mapstrategy
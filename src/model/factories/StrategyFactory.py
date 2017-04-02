
from src.utility import MetaSingleton


class StrategyFactory(metaclass=MetaSingleton):

    # TODO mettere in un file la lettura della strategy
    #_mapstrategy = FirstMapStrategy()

    def getMapStrategy(self):
        return self._mapstrategy
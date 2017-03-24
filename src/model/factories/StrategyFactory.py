from src.utility.mapstrategy.FirstMapStrategy import *


class StrategyFactory:

    _mapstrategy = FirstMapStrategy()

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)

        return cls._instance

    @classmethod
    def getInstance(cls):
        return cls.__new__()


    def getMapStrategy(self):
        return self._mapstrategy
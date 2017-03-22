class MatchMakingHandler:
    _instance = None  # singleton instance

    def __init__(self):
        if not MatchMakingHandler._instance:
            MatchMakingHandler._instance = self
        else:
            raise MatchMakingHandler._instance  # throw exception

    @staticmethod
    def getInstance():
        return MatchMakingHandler._instance

    def makeNewGame(self, player, modeid="nomode", isranked=False):
        pass

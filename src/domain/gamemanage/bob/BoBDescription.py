# TODO nella prossima iterazione, scegliere i parametri che deve avere il bob durante la partita

# TODO è un multiton

class BoBDescription():
    ########## ATTRIBUTES DEFINITION ##########
    # speed: speed of the Bobs upon the Map
    # maxplacedbombs: maximum number of bombs that could be placed (default)

    _descriptions = dict()  # singleton instance

    def __new__(cls, *args, **kwargs) -> 'BoBDescription':
        if cls._descriptions.get(args[0], None) is None:
            cls._descriptions[args[0]] = super().__new__(cls)

        return cls._descriptions.get(args[0])

    @classmethod
    def getDescription(cls, description: str) -> 'BoBDescription':
        """
        Gives an instance of the BoBDescrioption
        :param description: String ID of the BoBDescrioption
        :return: The selected BoBDescrioption
        """
        return cls.__new__(cls(), description)

    def __init__(self, descr: str):
        self._retrieveDescription(descr)

    def _retrieveDescription(self, descr: str):

        # TODO deve essere preso dal database

        if descr == "classic":
            self.speed = 8  # TODO  scegliere un'unità di misura rispetto alla grafica
            self.maxplacedbombs = 1  # max numero di bombe piazzabili
        else:
            self.speed = 10  # TODO  scegliere un'unità di misura rispetto alla grafica
            self.maxplacedbombs = 2  # max numero di bombe piazzabili

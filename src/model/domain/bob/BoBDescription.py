from src.utility.MetaSingleton import MetaSingleton

class BoBDescription(metaclass=MetaSingleton):

    ########## ATTRIBUTES DEFINITION ##########
    # _descr:
    _descr = None

    # TODO fare con multiton (unito a bobcatalog)?

    def getDescription(self):
        return self._descr
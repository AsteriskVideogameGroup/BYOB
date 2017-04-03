from src.utility.MetaSingleton import MetaSingleton

class BoBDescription(metaclass=MetaSingleton):

    ########## ATTRIBUTES DEFINITION ##########
    # _descr:

    def getDescription(self):
        return self._descr
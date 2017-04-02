from src.utility.MetaSingleton import MetaSingleton

class BoBDescription(metaclass=MetaSingleton):

    _descr = None

    def getDescription(self):
        return self._descr
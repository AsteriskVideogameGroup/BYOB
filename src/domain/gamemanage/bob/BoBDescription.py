from src.utility.metaclasses.MetaSingleton import MetaSingleton


class BoBDescription(metaclass=MetaSingleton):
    ########## ATTRIBUTES DEFINITION ##########
    # _descr:

    def getDescription(self):
        return self._descr

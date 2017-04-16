from src.utility.metaclasses.MetaSingleton import MetaSingleton


#TODO nella prossima iterazione, scegliere i parametri che deve avere il bob durante la partita

#TODO è un multiton

class BoBDescription(metaclass=MetaSingleton):
    ########## ATTRIBUTES DEFINITION ##########
    # _descr:

    def getDescription(self):
        return self._descr

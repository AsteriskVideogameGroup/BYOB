from src.model.domain.gamemode import Mode
from src.utility import MetaSingleton, Dimensions


class GameModeFactory(metaclass=MetaSingleton):

    def getGameMode(self, modeid: str) -> Mode:
        """
        Translate the gamemode ID in the selected GameMode and add it tho _modes
        :param modeid: String ID of the GameMode
        """

        #  MODES = 'modes'  # name of the mode setting modelist = GlobalSettings().getSetting(MODES)  # list of all
        #  available modes TODO eliminare perché non serve
        #  newmodeclass = globals()[modelist.get(modeid)] TODO rimuovere
        #  instantiare the new modality (remember that it's simgleton) TODO rimuovere

        # TODO dobbiamo prendere i dati da un database
        newmode = Mode(Dimensions(5, 7), None, 4, 3, 300)

        return newmode

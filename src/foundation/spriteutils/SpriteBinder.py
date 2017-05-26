from src.foundation.metaclasses.MetaSingleton import MetaSingleton
from src.foundation.settings.GlobalSettings import GlobalSettings


class SpriteBinder(metaclass=MetaSingleton):
    _SPRITEPATHSETTING = "spritepath"

    def __init__(self):
        self._spritepath = GlobalSettings().getSetting(SpriteBinder._SPRITEPATHSETTING)

    def wrapSprite(self, logicalmapelement):
        """
        Wrap an IMapElement into a GraphicalIMapElement
        :param logicalmapelement: Element to be wrapped
        """
        pass  # TODO effettuare il binding

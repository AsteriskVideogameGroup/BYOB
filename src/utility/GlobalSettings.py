import json
from src.utility import MetaSingleton


class GlobalSettings(metaclass=MetaSingleton):
    def __new__(cls, *args, **kwargs) -> 'MatchMakingHandler':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._settingpath = "../settings/programsettings.json"
        self._settings = dict()
        self._setup()

    def getSetting(self, setting: str) -> dict:
        """
        Retrieve the speciefied global setting
        :param setting: Setting to be got
        :return: Dictionary of settings (returns empty dict if setting doesn't exist)
        """
        return self._settings.get(setting)

    def _setup(self):
        with open(self._settingpath) as settings_file:
            self._settings = {**self._settings, **json.load(settings_file)}
            # print(self._settings['modes'])




class Config:

    def __init__(self, config):
        self._config = config

    def is_not_set(self, key):
        return self.value().upper() == "NOT_SET"

    def value(self, key):
        return self._config[key.upper()]
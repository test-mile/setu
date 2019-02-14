from .config_types import SetuConfigOption

class Config:

    def __init__(self, config_enum_class, config_dict):
        self.__key_enum_class = config_enum_class
        self.__config_dict = {}
        for k,v in config_dict.items():
            try:
                e_key = config_enum_class[k.upper()]
            except:
                raise Exception("input dictionary contains key: {} which is not a valid {} constant.".format(k, config_enum_class))
            else:
                self.__config_dict[e_key] = v

    def __validate_enum_key(self, key):
        if not isinstance(key, self.__key_enum_class):
            raise Exception("Key must be an enum consts of type: {}".format(self.__key_enum_class))

    def is_not_set(self, key):
        self.__validate_enum_key(key)
        return self.value(key).upper() == "NOT_SET"

    def value(self, key):
        self.__validate_enum_key(key)
        return self.__config_dict[key]

    def as_json_dict(self):
        return {k.name: v for k,v in self.__config_dict.items()}


class SetuConfig(Config):

    def __init__(self, config_dict):
        super().__init__(SetuConfigOption, config_dict)
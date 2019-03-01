from enum import Enum
from setu.core.constants import *

from setu.core.lib.setu_types import SetuManagedObject

class Config(SetuManagedObject):
    DESKTOP_CONTEXTS = {GuiAutomationContext.NATIVE, GuiAutomationContext.WEB}
    MOBILE_WEB_CONTEXTS = {GuiAutomationContext.ANDROID_WEB, GuiAutomationContext.IOS_WEB}
    ALL_WEB_CONTEXTS = {GuiAutomationContext.WEB, GuiAutomationContext.ANDROID_WEB, GuiAutomationContext.IOS_WEB}
    MOBILE_NATIVE_CONTEXTS = {GuiAutomationContext.ANDROID_NATIVE, GuiAutomationContext.IOS_NATIVE}

    def __init__(self):
        super().__init__()
        self.__setu_config = None
        self.__user_config = None

    @property
    def setu_config(self):
        return self.__setu_config

    @setu_config.setter
    def setu_config(self, conf):
        self.__setu_config = conf

    @property
    def user_config(self):
        return self.__user_config

    @user_config.setter
    def user_config(self, conf):
        self.__user_config = conf

    def as_json_dict(self):
        return {
            "setuOptions" : self.__setu_config.as_json_dict(),
            "userOptions" : self.__user_config.as_json_dict()
        }

class AbstractConfig:

    def __init__(self, config_dict):
        self.__config_dict = config_dict

    @property
    def _config_dict(self):
        return self.__config_dict

    def is_not_set(self, key):
        self._validate_key(key)
        try:
            return self.value(key).upper() == "NOT_SET"
        except:
            return False

    def _validate_key(self, key):
        pass

    def value(self, key):
        self._validate_key(key)
        return self.__config_dict[key]

    def as_map(self):
        return self.__config_dict

    def __as_enum_name_or_same(self, input):
        if isinstance(input, Enum):
            return input.name
        else:
            return input

    def as_json_dict(self):
        return {k:self.__as_enum_name_or_same(v) for k,v in self.as_map().items()}

    def get_guiauto_context(self):
        return GuiAutomationContext[self.value(SetuConfigOption.GUIAUTO_CONTEXT).upper()]

    def has_desktop_context(self):
        return self.get_guiauto_context() in Config.DESKTOP_CONTEXTS

    def has_mobile_web_context(self):
        return self.get_guiauto_context() in Config.MOBILE_WEB_CONTEXTS

    def has_mobile_native_context(self):
        return self.get_guiauto_context() in Config.MOBILE_NATIVE_CONTEXTS

    def has_web_context(self):
        return self.get_guiauto_context() in Config.ALL_WEB_CONTEXTS

class UserConfig(AbstractConfig):

    def __init__(self, config_dict):
        super().__init__(config_dict)

class SetuConfig(AbstractConfig):

    def __init__(self, config_dict):
        super().__init__(config_dict)

    def _validate_key(self, key):
        if not isinstance(key, SetuConfigOption):
            raise Exception("Key must be an enum consts of type SetuConfigOption")

    def as_json_dict(self):
        out = {k.name: v for k,v in super().as_json_dict().items()}
        print(out)
        return out
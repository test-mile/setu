import os
import copy
from trishanku.tpi.reader.hocon import HoconFileReader, HoconStringReader, HoconConfigDictReader

from setu.core.constants import SetuConfigOption
from .validator import ConfigValidator
from .config import Config, SetuConfig, UserConfig
from pprint import pprint

class ConfigCreator:
    SETU_CONF_DESC_MAP = None

    @classmethod
    def init(cls):
        if cls.SETU_CONF_DESC_MAP is not None:
            return
        my_dir = os.path.dirname(os.path.realpath(__file__))
        setu_conf_desc_file = os.path.join(my_dir, "..", "res", "setu_config_desc.conf")  
        cls.__process_setu_conf_desc(setu_conf_desc_file)  

    @classmethod
    def __process_setu_conf_desc(cls, type_path):
        cls.SETU_CONF_DESC_MAP = cls.get_flat_map_from_hocon_string_for_setu_types(
            HoconFileReader(type_path)
        )    

    @classmethod
    def __setu_conf_key(cls, key):
        try:
            return SetuConfigOption[key]
        except Exception:
            raise Exception("Config option [{}] is not a valid SetuConfigOption constant".format(key))

    @classmethod
    def __get_flat_map_from_hocon_string(cls, hreader):
        hreader.process()
        return {i.upper().strip().replace(".","_"):j for i,j in hreader.get_flat_map().items()}

    @classmethod      
    def get_flat_map_from_hocon_string_for_setu_types(cls, hreader):
        return {cls.__setu_conf_key(k):v for k,v in cls.__get_flat_map_from_hocon_string(hreader).items()}

    @classmethod
    def create_config_for_raw_map(self, map, validator_func):
        out_map = {}
        for conf_name, raw_value in map.items():
            validator_name, validator = validator_func(conf_name)
            try:
                is_not_set = False
                try:
                    is_not_set = raw_value.lower() == "not_set"
                except:
                    pass
                finally:
                    if is_not_set:
                        out_map[conf_name] = "not_set"
                    else:
                        out_map[conf_name] = validator(raw_value)
            except:
                raise Exception("Config option value [{}](type:{}) for [{}] option did not pass the validation check: [{}]".format(
                    raw_value, type(raw_value), conf_name, validator_name)
                )
        return out_map

    @classmethod
    def create_conf(cls, processor, setu_conf, user_conf):
        config = Config()
        config.setu_config = SetuConfig(setu_conf)
        config.user_config = UserConfig(user_conf)
        config.processor = processor
        return config

    @classmethod
    def __create_new_conf(cls, processor, source, setu_dict=None, user_dict=None):
        out_setu = copy.deepcopy(source.setu_config.as_map())
        out_user = copy.deepcopy(source.user_config.as_map())
        if setu_dict:
            out_setu.update(setu_dict)
        if user_dict:
            out_user.update(user_dict)
        return cls.create_conf(processor, out_setu, out_user)

    @classmethod
    def create_new_conf(cls, processor, source, cdict):
        if not cdict:
            return cls.__create_new_conf(processor, source)

        custom_setu_conf = None
        if "setuOptions" in cdict:
            # setuOptions
            custom_raw_setu_config_map = cls.get_flat_map_from_hocon_string_for_setu_types(
                HoconConfigDictReader(cdict["setuOptions"])
            )
            custom_setu_conf = cls.create_config_for_raw_map(custom_raw_setu_config_map, processor.get_setu_option_validator)

        custom_user_conf = None
        if "userOptions" in cdict:
            project_raw_user_config_map = cls.__get_flat_map_from_hocon_string(
                HoconConfigDictReader(cdict["userOptions"])
            )
            custom_user_conf = cls.create_config_for_raw_map(
                project_raw_user_config_map, 
                processor.get_user_option_validator
            )
        return cls.__create_new_conf(processor, source, custom_setu_conf, custom_user_conf) 

class BaseConfigProcessor:

    def __init__(self):
        self.__setu_type_map = {}
        self.__config = None

    @property
    def config(self):
        return self.__config

    @config.setter
    def _config(self, config):
        self.__config = config

    def pass_through(self, input):
        return input

    def get_setu_option_validator(self, conf_name):
        validator_name = ConfigCreator.SETU_CONF_DESC_MAP[conf_name]
        return validator_name, getattr(ConfigValidator, validator_name.lower())

    def get_user_option_validator(self, conf_name):
        return "pass_through", self.pass_through

class CentralConfigLoader(BaseConfigProcessor):

    def __init__(self, root_dir):
        my_dir = os.path.dirname(os.path.realpath(__file__))
        self.__setu_central_confg_file = os.path.join(my_dir, "..", "res", "setu_central.conf")
        self.root_dir = root_dir
        self.__process()

    def __process(self):
        # Processes central conf based on root directory
        f = open(self.__setu_central_confg_file, "r")
        contents = f.read()
        f.close()
        contents = contents.replace("<ROOT_DIR>", self.root_dir)
        raw_config_map = ConfigCreator.get_flat_map_from_hocon_string_for_setu_types(
            HoconStringReader(contents)
        )
        pprint(raw_config_map)
        self._config = ConfigCreator.create_conf(
            self,
            ConfigCreator.create_config_for_raw_map(raw_config_map, self.get_setu_option_validator), 
            {}
        )
        pprint(self.config.as_json_dict())

class ProjectConfigCreator(BaseConfigProcessor):

    def __init__(self, central_conf):
        self.__central_conf = central_conf
        self.__process()

    def __process(self):
        # Process project conf
        project_conf_file = self.__central_conf.setu_config.value(SetuConfigOption.PROJECT_CONF_FILE)
        project_hreader = HoconFileReader(project_conf_file)
        project_hreader.process()
        cdict = project_hreader.get_map()

        self._config = ConfigCreator.create_new_conf(self, self.__central_conf, cdict)




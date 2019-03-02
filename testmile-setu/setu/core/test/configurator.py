
from setu.core.config.processor import ConfigCreator, CentralConfigLoader, ProjectConfigCreator
from setu.core.constants import SetuConfigOption
from trishanku.tpi.reader.hocon import HoconStringReader

class TestConfigurator:
    
    def __init__(self):
        self.__default_ref_config = None 
        self.__config_map = {}

    def init(self, root_dir):
        self.__default_ref_config = CentralConfigLoader(root_dir).config
        self.__config_map[self.__default_ref_config.setu_id] = self.__default_ref_config
        return self.__default_ref_config.setu_id

    def create_project_config(self):
        project_conf_loader = ProjectConfigCreator(self.__default_ref_config)
        self.__default_ref_config = project_conf_loader.config
        self.__default_ref_config.process_setu_options()
        self.__config_map[self.__default_ref_config.setu_id] = self.__default_ref_config
        return self.__default_ref_config.setu_id

    def get_config(self, setu_id):
        return self.__config_map[setu_id]

    def get_setu_option_value(self, config_setu_id, option):
        return self.__config_map[config_setu_id].setu_config.value(SetuConfigOption[option.upper().strip().replace(".","_")])

    def register_config(self, setu_options, user_options=None):
        config = ConfigCreator.create_new_conf(
            self.__default_ref_config.processor, 
            self.__default_ref_config,
            HoconStringReader(str({
                "setuOptions" : setu_options,
                "userOptions" : user_options
            })).get_map()
        )
        config.process_setu_options()
        self.__config_map[config.setu_id] = config
        return config.setu_id


    

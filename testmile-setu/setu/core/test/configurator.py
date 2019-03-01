
from setu.core.config.processor import CentralConfigLoader, ProjectConfigCreator

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
        self.__config_map[self.__default_ref_config.setu_id] = self.__default_ref_config
        return self.__default_ref_config.setu_id

    def get_config(self, setu_id):
        return self.__config_map[setu_id]

    

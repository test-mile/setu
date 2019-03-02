

# Arg names of methods show JSON names, so don't follow Python conventions.
class TestSessionConfHandler:

    def __init__(self, configurator):
        self.__configurator = configurator

    def get_setu_option_value(self, configSetuId, option):
        return {"value" : self.__configurator.get_setu_option_value(configSetuId, option)}

    def register_config(self, setuOptions, hasParent, userOptions=None, parentConfigId=None):
        return {"configSetuId" : self.__configurator.register_config(setuOptions, hasParent, userOptions, parentConfigId)}

    def load_project_conf(self):
        return {"configSetuId" : self.__configurator.create_project_conf()}


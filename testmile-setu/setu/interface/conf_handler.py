

# Arg names of methods show JSON names, so don't follow Python conventions.
class TestSessionConfHandler:

    def __init__(self, configurator):
        self.__configurator = configurator

    def get_setu_option_value(self, configSetuId, option):
        return {"value" : self.__configurator.get_setu_option_value(configSetuId, option)}


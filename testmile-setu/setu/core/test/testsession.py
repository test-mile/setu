from setu.core.lib.setu_types import SetuManagedObject
from setu.core.test.configurator import TestConfigurator

class TestSession(SetuManagedObject):

    def __init__(self):
        super().__init__()
        self.__configurator = TestConfigurator()

    @property
    def configurator(self):
        return self.__configurator

    def init(self, root_dir):
        return self.__configurator.init(root_dir)
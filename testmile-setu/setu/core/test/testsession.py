from setu.core.lib.setu_types import SetuManagedObject
from setu.core.test.configurator import TestConfigurator
from setu.core.data_broker.databroker import DataBroker

class TestSession(SetuManagedObject):

    def __init__(self):
        super().__init__()
        self.__configurator = TestConfigurator()
        self.__data_broker = DataBroker()

    @property
    def configurator(self):
        return self.__configurator

    @property
    def data_broker(self):
        return self.__data_broker

    def init(self, root_dir):
        return self.__configurator.init(root_dir)
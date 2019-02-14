import abc

from setu.core.guiauto.base.element_container import ElementContainer

class BaseElement(ElementContainer, metaclass=abc.ABCMeta):
    def __init__(self, automator, emd):
        super().__init__(automator.config, automator.agent_requester)
        self.__automator = automator
        self.__emd = emd
        self.__found = False
        self.__located_by = None 

    @abc.abstractmethod
    def find_if_not_found(self):
        pass

    def get_locator_meta_data(self):
        return self.__emd

    def is_found(self):
        return self.__found

    def set_found_with(self, locator_type, locator_value):
        self.__found = True
        self.__located_by = locator_type, locator_value

    def get_found_with(self, locator_type, locator_value):
        return self.__located_by

    def get_automator(self):
        return self.__automator
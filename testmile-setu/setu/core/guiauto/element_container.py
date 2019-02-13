import abc

from setu.core.lib.setu_types import SetuAgentProxy

from .emd import SimpleGuiElementMetaData
from .finder_actions import FinderActions


class ElementContainer(SetuAgentProxy, metaclass=abc.ABCMeta):
    def __init__(self, agent_requster):
        super().__init__(agent_requster)
        self.element_map = {}
        self.melement_map = {}

    def _add_element(self, setu_id, element):
        self.element_map[setu_id] = element

    def _add_multielement(self, setu_id, melement):
        self.melement_map[setu_id] = melement

    def create_element(self, locator_meta_data):
        from .element import GuiElement
        elem = GuiElement(self, locator_meta_data)
        self._add_element(elem.get_setu_id(), elem)
        print(elem.get_setu_id())
        return elem

    def create_element_with_locator(self, locator_name, locator_value):
        return self.create_element(SimpleGuiElementMetaData(locator_name, locator_value))

    def create_multielement(self, locator_meta_data):
        from .multielement import GuiMultiElement
        element = GuiMultiElement(self, locator_meta_data)
        self._add_multielement(element.get_setu_id(), element)
        return element

    def create_multielement_with_locator(self, locator_name, locator_value):
        return self.create_multielement(SimpleGuiElementMetaData(locator_name, locator_value))

    def __find(self, creator_func, gui_element):
        found = False
        print(gui_element.get_setu_id())
        for locator_type, locator_value in gui_element.get_locator_meta_data().get_locators(): 
            print("hh", locator_type, locator_value)
            try:
                body = self._act(creator_func(
                    uuid=gui_element.get_setu_id(),
                    byType=locator_type,
                    byValue=locator_value
                ))
                return locator_type, locator_value, body
            except Exception as e:
                print("dfgdfkjghdfkjghdkjgh")
                print(e)
                continue
        print("outside")
        if not found:
            raise Exception("Could not locate element with locator(s): {}".format(gui_element.get_locator_meta_data().get_locators()))

    def find_element(self, gui_element):
        print("hkjhh")
        locator_type, locator_value, __ = self.__find(FinderActions.find_first_element, gui_element)
        gui_element.set_found_with(locator_type, locator_value)

    def find_multielement(self, gui_element):
        locator_type, locator_value, body = self.__find(FinderActions.find_multi_element, gui_element)
        gui_element.set_found_with(locator_type, locator_value)
        gui_element.set_instance_count(body["data"]["instanceCount"])

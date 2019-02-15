import abc

from setu.core.lib.setu_types import SetuAgentProxy

from setu.core.guiauto.locator.emd import SimpleGuiElementMetaData
from setu.core.guiauto.actions.finder_actions import FinderActions

from .container_conditions import GuiElementContainerConditions

class ElementContainer(SetuAgentProxy, metaclass=abc.ABCMeta):
    def __init__(self, config, agent_requester):
        super().__init__(config, agent_requester)
        self.element_map = {}
        self.melement_map = {}
        self.__container_conditions = GuiElementContainerConditions(self)

    def _add_element(self, setu_id, element):
        self.element_map[setu_id] = element

    def _add_multielement(self, setu_id, melement):
        self.melement_map[setu_id] = melement

    def create_element(self, locator_meta_data):
        from setu.core.guiauto.element.guielement import GuiElement
        elem = GuiElement(self, locator_meta_data)
        self._add_element(elem.get_setu_id(), elem)
        print(elem.get_setu_id())
        return elem

    def create_element_with_locator(self, locator_name, locator_value):
        return self.create_element(SimpleGuiElementMetaData(locator_name, locator_value))

    def create_multielement(self, locator_meta_data):
        from setu.core.guiauto.element.multielement import GuiMultiElement
        element = GuiMultiElement(self, locator_meta_data)
        self._add_multielement(element.get_setu_id(), element)
        return element

    def create_multielement_with_locator(self, locator_name, locator_value):
        return self.create_multielement(SimpleGuiElementMetaData(locator_name, locator_value))

    def _find(self, gui_element):
        found = False
        for locator_type, locator_value in gui_element.get_locator_meta_data().get_locators(): 
            try:
                body = self._act(FinderActions.find_multi_element(
                    uuid=gui_element.get_setu_id(),
                    byType=locator_type,
                    byValue=locator_value
                ))
                return locator_type, locator_value, body
            except Exception as e:
                continue
        if not found:
            raise Exception("Could not locate elements with locator(s): {}".format(gui_element.get_locator_meta_data().get_locators()))

    def wait_until_found(self, gui_element):
        return self.__container_conditions.PresenceOf(gui_element).wait()

    def find_multielement(self, gui_element):
        locator_type, locator_value, body = self.wait_until_found(gui_element)
        gui_element.set_found_with(locator_type, locator_value)
        gui_element.set_instance_count(body["data"]["instanceCount"])

    def find_element(self, gui_element):
        locator_type, locator_value, __ = self.wait_until_found(gui_element)
        gui_element.set_found_with(locator_type, locator_value)
        self._act(FinderActions.retain_first_element(uuid=gui_element.get_setu_id()))

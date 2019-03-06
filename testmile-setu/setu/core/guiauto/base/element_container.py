import abc

from setu.core.lib.setu_types import SetuConfiguredObject

from setu.core.guiauto.locator.emd import SimpleGuiElementMetaData

from .container_conditions import GuiElementContainerConditions

class ElementContainer(SetuConfiguredObject, metaclass=abc.ABCMeta):
    def __init__(self, config):
        super().__init__(config)
        self.element_map = {}
        self.melement_map = {}
        self.__container_conditions = GuiElementContainerConditions(self)

    def _add_element(self, setu_id, element):
        self.element_map[setu_id] = element

    def _add_multielement(self, setu_id, melement):
        self.melement_map[setu_id] = melement

    def get_element_for_setu_id(self,id):
        return self.element_map[id]

    def get_multielement_for_setu_id(self,id):
        return self.melement_map[id]

    def create_element(self, locator_meta_data):
        from setu.core.guiauto.element.guielement import GuiElement
        elem = GuiElement(self, locator_meta_data)
        self._add_element(elem.get_setu_id(), elem)
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

    def create_dropdown_with_locator(self, locator_name, locator_value):
        from setu.core.guiauto.element.dropdown import GuiWebSelect
        select = GuiWebSelect(self, locator_name, locator_value)
        self._add_element(select.get_setu_id(), select)
        return select

    def create_radiogroup_with_locator(self, locator_name, locator_value):
        from setu.core.guiauto.element.radio_group import GuiWebRadioGroup
        rg = GuiWebRadioGroup(self, locator_name, locator_value)
        self._add_element(rg.get_setu_id(), rg)
        return rg

    def _find(self, json_creator, gui_element):
        found = False
        for locator_type, locator_value in gui_element.get_locator_meta_data().get_locators(): 
            try:
                body = self._act(json_creator(
                    uuid=gui_element.get_setu_id(),
                    byType=locator_type,
                    byValue=locator_value
                ))
                return locator_type, locator_value, body
            except Exception as e:
                continue
        if not found:
            raise Exception("Could not locate elements with locator(s): {}".format(gui_element.get_locator_meta_data().get_locators()))

    def wait_until_element_found(self, gui_element):
        return self.__container_conditions.PresenceOfElement(gui_element).wait()

    def wait_until_multielement_found(self, gui_element):
        return self.__container_conditions.PresenceOfMultiElement(gui_element).wait()

    def find_multielement(self, gui_element):
        locator_type, locator_value, body = self.wait_until_multielement_found(gui_element)
        gui_element.set_found_with(locator_type, locator_value)
        gui_element.set_instance_count(body["data"]["instanceCount"])

    def find_element(self, gui_element):
        locator_type, locator_value, __ = self.wait_until_element_found(gui_element)
        gui_element.set_found_with(locator_type, locator_value)

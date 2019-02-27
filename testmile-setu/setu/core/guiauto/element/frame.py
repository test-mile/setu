from setu.core.lib.setu_types import SetuManagedObject
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator

# UUID is for client reference. Agent does not know about this.
class IFrameWithElement(SetuManagedObject):

    def __init__(self, gui_main_element: GuiElement):
        super().__init__()
        self._wrapped_main_element = gui_main_element
        tag = self._wrapped_main_element.get_tag_name()
        if tag.lower() != "iframe":
            raise Exception("The element should have a 'iframe' tag for IFrame element. Found: " + tag)
        self.__first_level = True
        self.__parent_frames = []
        self.__automator = gui_main_element.get_automator()

    def _act(self, json_dict):
        return self.__automator.actor_callable(json_dict)

    def switch_to_frame_by_name(self, name):
        self._act(TestAutomatorActionBodyCreator.switch_to_frame_by_name(name))

    def switch_to_frame_by_index(self, index):
        self._act(TestAutomatorActionBodyCreator.switch_to_frame_by_index(index))

    def switch_to_parent_frame(self):
        self._act(TestAutomatorActionBodyCreator.switch_to_parent_frame())

    def switch_to_root(self):
        self._act(TestAutomatorActionBodyCreator.switch_to_root())

    def switch_to_frame_of_element(self, element):
        element.find_if_not_found()
        self._act(TestAutomatorActionBodyCreator.switch_to_frame_of_element(element))

    def switch_to_parent(self):
        self.__automator.se

    def __is_multi_select(self):
        return self._wrapped_main_element.get_attr_value("multiple") is True or self._wrapped_main_element.get_attr_value("multi") is True
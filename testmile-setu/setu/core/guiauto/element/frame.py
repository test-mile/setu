from setu.core.lib.setu_types import SetuManagedObject
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator

# UUID is for client reference. Agent does not know about this.
class IFrame(SetuManagedObject):

    def __init__(self, automator, locator_name, locator_value):
        super().__init__()
        self._multi_element = None
        if locator_name.lower() == "index":
            index = int(locator_value)
            self._multi_element = automator.create_multielement_with_locator("xpath", "//iframe")
            self._multi_element.find()
            self._wrapped_main_element = self._multi_element.get_instance_at_index(index)
        else:
            self._wrapped_main_element = automator.create_element_with_locator(locator_name, locator_value)
        tag = self._wrapped_main_element.get_tag_name()
        if tag.lower() != "iframe":
            raise Exception("The element should have a 'iframe' tag for IFrame element. Found: " + tag)
        self.__parent_frames = []
        self.__automator = automator

    def set_parents(self, parents):
        self.__parent_frames = parents

    def _act(self, json_dict):
        return self.__automator.actor_callable(json_dict)

    def jump(self):
        if self.__parent_frames:
            for parent in self.__parent_frames:
                parent.switch()

        # Handle frame by index
        if self._multi_element:
            self._multi_element.find()
            self._act(TestAutomatorActionBodyCreator.jump_to_frame(
                self._multi_element,
                **self.get_instance_dict())
        )
        else:
            self._wrapped_main_element.find()
            self._act(TestAutomatorActionBodyCreator.jump_to_frame(
                self._wrapped_main_element,
                **self.get_instance_dict())
            )
        self.__automator.set_frame_context(self)

    def jump_to_child(self, locator_name, locator_value):
        frame = IFrame(self.__automator, locator_name, locator_value)
        frame.set_parents(self.__parent_frames + [self])
        frame.jump()
        self.__automator.set_frame_context(frame)

    def jump_to_parent(self):
        self._act(TestAutomatorActionBodyCreator.jump_to_parent_frame())
        if self.__parent_frames:
            self.__automator.set_frame_context(self.__parent_frames[-1])
        else:
            self.__automator.set_frame_context_as_root()

    def jump_to_root(self):
        self._act(TestAutomatorActionBodyCreator.jump_to_html_root())
        self.__automator.set_frame_context_as_root()

    def get_instance_dict(self):
        d = {}
        if self._multi_element:
            d["isInstanceAction"] = True
            d["instanceIndex"] = self._wrapped_main_element._get_instance_number()
        else:
            d["isInstanceAction"] = False
        return d
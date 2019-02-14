from setu.core.config.config_utils import Config
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator
from .handler import Handler

class FrameHandler(Handler):

    def __init__(self, automator):
        super().__init__(automator)

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


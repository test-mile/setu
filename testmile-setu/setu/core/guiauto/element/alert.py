from setu.core.lib.setu_types import SetuManagedObject
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator
from setu.core.constants import SetuConfigOption

class Alert(SetuManagedObject):

    def __init__(self, automator):
        super().__init__()
        self.__automator = automator

    @property
    def automator(self):
        return self.__automator

    def _act(self, json_dict):
        return self.__automator.actor_callable(json_dict)

    def confirm(self):
        self._act(TestAutomatorActionBodyCreator.confirm_alert())
        self.automator.alert_handler.delete_alert()

    def dismiss(self):
        self._act(TestAutomatorActionBodyCreator.dismiss_alert())
        self.automator.alert_handler.delete_alert()

    def send_text(self, text):
        self._act(TestAutomatorActionBodyCreator.send_text_to_alert(text))

    def get_text(self):
        response = self._act(TestAutomatorActionBodyCreator.get_text_from_alert())
        return response["data"]["text"]
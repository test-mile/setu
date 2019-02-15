from setu.core.config.config_utils import Config
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator
from .handler import Handler

class AlertHandler(Handler):

    def __init__(self, automator):
        super().__init__(automator)

    def wait_for_alert(self):
        self.automator.conditions.AlertIsPresent().wait()

    def is_alert_present(self):
        response = self._act(TestAutomatorActionBodyCreator.is_alert_present())
        return response["data"]["checkResult"]

    def confirm_alert(self):
        self.wait_for_alert()
        self._act(TestAutomatorActionBodyCreator.confirm_alert())

    def dismiss_alert(self):
        self.wait_for_alert()
        self._act(TestAutomatorActionBodyCreator.dismiss_alert())

    def send_text_to_alert(self, text):
        self.wait_for_alert()
        self._act(TestAutomatorActionBodyCreator.send_text_to_alert(text))

    def get_text_from_alert(self):
        self.wait_for_alert()
        response = self._act(TestAutomatorActionBodyCreator.get_text_from_alert())
        return response["data"]["text"]


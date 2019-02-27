from setu.core.config.config_utils import Config
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator
from .handler import Handler

class AlertHandler(Handler):

    def __init__(self, automator):
        super().__init__(automator)
        self.__alert_present = False
        self.__alert_setu_id = None
        self.__alert = None

    def create_alert(self):
        if self.__alert_present:
            return self.__alert
        else:
            self.wait()
            from setu.core.guiauto.element.alert import Alert
            self.__alert_present = True
            alert = Alert(self.automator)
            self.__alert_setu_id = alert.setu_id
            self.__alert = alert
            return alert

    def get_alert_for_setu_id(self, setu_id):
        msg = "The alert represented by this object no longer exists."
        if not self.__alert_present:
            raise Exception(msg)
        elif self.__alert_setu_id != setu_id:
            raise Exception(msg)
        else:
            return self.__alert

    def delete_alert(self):
        self.__alert_present = False
        self.__alert_setu_id = None
        self.__alert = None

    def wait(self):
        self.automator.conditions.AlertIsPresent().wait()

    def is_alert_present(self):
        response = self._act(TestAutomatorActionBodyCreator.is_alert_present())
        return response["data"]["checkResult"]




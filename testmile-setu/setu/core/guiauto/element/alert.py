from setu.core.lib.setu_types import SetuManagedObject
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.constants import SetuConfigOption

class Alert(SetuManagedObject):

    def __init__(self, automator):
        super().__init__()
        self.__automator = automator

    @property
    def automator(self):
        return self.__automator

    def confirm(self):
        self.automator.dispatcher.confirm_alert()
        self.automator.alert_handler.delete_alert()

    def dismiss(self):
        self.automator.dispatcher.dismiss_alert()
        self.automator.alert_handler.delete_alert()

    def send_text(self, text):
        self.automator.dispatcher.send_text_to_alert(text)

    def get_text(self):
        return self.automator.dispatcher.get_text_from_alert()
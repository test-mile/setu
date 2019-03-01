from setu.core.guiauto.actions.automator_actions import \
    TestAutomatorActionBodyCreator
from setu.core.constants import SetuConfigOption

from .guiautomator import GuiAutomator
from .handler import Handler

class BrowserNavigator(Handler):

    def __init__(self, automator: GuiAutomator):
        super().__init__(automator)

    def to(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to(url=url))
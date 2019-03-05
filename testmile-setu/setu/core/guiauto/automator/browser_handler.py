from setu.core.guiauto.actions.automator_actions import \
    TestAutomatorActionBodyCreator
from setu.core.constants import SetuConfigOption

from .guiautomator import GuiAutomator
from .handler import Handler

class BrowserHandler(Handler):

    def __init__(self, automator: GuiAutomator):
        super().__init__(automator)

    def go_to_url(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def go_back(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def go_forward(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def refresh(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))
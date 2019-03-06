from setu.core.guiauto.actions.automator_actions import \
    TestAutomatorActionBodyCreator
from setu.core.constants import SetuConfigOption

from .guiautomator import GuiAutomator
from .handler import Handler

class Browser(Handler):

    def __init__(self, automator: GuiAutomator):
        super().__init__(automator)
        from setu.core.guiauto.element.frame import DomRoot
        self.__dom_root = DomRoot(automator)

    @property
    def dom_root(self):
        return self.__dom_root

    def go_to_url(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def go_back(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def go_forward(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def refresh(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to_url(url=url))

    def execute_javascript(self, js):
        self._act(TestAutomatorActionBodyCreator.execute_javascript(js))
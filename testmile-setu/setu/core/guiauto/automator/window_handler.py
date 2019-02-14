from setu.core.config.config_utils import Config
from setu.core.guiauto.actions.automator_actions import \
    TestAutomatorActionBodyCreator
from setu.core.config.config_types import SetuConfigOption

from .guiautomator import GuiAutomator
from .handler import Handler

class WindowHandler(Handler):

    def __init__(self, automator: GuiAutomator):
        super().__init__(automator)
        self._main_win_handle = self.get_current_window_handle()

    def resize_window_as_per_config(self):
        # Resize window
        config = self.config
        browser_width = config.value(SetuConfigOption.BROWSER_DIM_WIDTH)
        browser_height = config.value(SetuConfigOption.BROWSER_DIM_HEIGHT)
        should_maximize = config.value(SetuConfigOption.BROWSER_MAXIMIZE)

        if config.is_not_set(browser_width) and config.is_not_set(browser_height):
            if should_maximize:
                self.maximize_window()
        else:
            width, height = None, None
            current_width, current_height = self.get_current_window_size()
            width = config.is_not_set(browser_width) and browser_width or current_width
            height = config.is_not_set(browser_height) and browser_height or current_height
            self.set_window_size(width, height)

    def get_all_child_window_handles(self):
        all_handles = self.get_all_window_handles()
        return [handle for handle in all_handles if handle != self._main_win_handle]

    def switch_to_new_window(self):
        all_child_handles = self.get_all_child_window_handles()
        if not all_child_handles:
            raise Exception("No new window was launched.")
        self.switch_to_window(all_child_handles[0])

    def switch_to_main_window(self):
        self.switch_to_window(self._main_win_handle)

    def switch_to_window(self, handle):
        self._act(TestAutomatorActionBodyCreator.switch_to_window(handle))

    def close_all_child_windows(self):
        for handle in self.get_all_child_window_handles():
            self.switch_to_window(handle)
            self.close_current_window()
        self.switch_to_main_window()

    def get_window_title(self):
        response = self._act(TestAutomatorActionBodyCreator.get_window_title())
        return response["data"]["title"]

    def get_current_window_handle(self):
        response = self._act(TestAutomatorActionBodyCreator.get_current_window_handle())
        return response["data"]["handle"]

    def maximize_window(self):
        self._act(TestAutomatorActionBodyCreator.maximize_window())

    def get_current_window_size(self):
        response = self._act(TestAutomatorActionBodyCreator.get_current_window_size())
        size = response["data"]["size"]
        return size["width"], size["height"]

    def set_window_size(self, width, height):
        self._act(TestAutomatorActionBodyCreator.set_window_size(width, height))

    def get_all_window_handles(self):
        response = self._act(TestAutomatorActionBodyCreator.get_all_window_handles())
        return response["data"]["handles"]

    def is_main_window(self):
        return self.get_current_window_handle() == self._main_win_handle

    def close_current_window(self):
        if not self.is_main_window():
            self._act(TestAutomatorActionBodyCreator.close_current_window())
            self.switch_to_main_window()

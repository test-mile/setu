from setu.core.lib.setu_types import SetuManagedObject
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.guiauto.actions.automator_actions import TestAutomatorActionBodyCreator
from setu.core.constants import SetuConfigOption

class BasicWindow(SetuManagedObject):

    def __init__(self, automator):
        super().__init__()
        self.__automator = automator
        self.__window_id = None
        self.__config = automator.config

    @property
    def config(self):
        return self.__config    

    @property
    def automator(self):
        return self.__automator

    @property
    def handle(self):
        return self.__window_id

    def _set_handle(self, handle):
        self.__window_id = handle

    def _act(self, json_dict):
        return self.__automator.actor_callable(json_dict)

    def jump(self):
        self._act(TestAutomatorActionBodyCreator.switch_to_window(self.handle))

    def is_main_window(self):
        return False

    def set_window_size(self, width, height):
        self._act(TestAutomatorActionBodyCreator.set_window_size(width, height))

    def maximize(self):
        self._act(TestAutomatorActionBodyCreator.maximize_window())

    def get_title(self):
        response = self._act(TestAutomatorActionBodyCreator.get_window_title())
        return response["data"]["title"]

    def get_size(self):
        response = self._act(TestAutomatorActionBodyCreator.get_current_window_size())
        size = response["data"]["size"]
        return size["width"], size["height"]

class MainWindow(BasicWindow):

    def __init__(self, automator, win_handle):
        super().__init__(automator)
        self._set_handle(win_handle)
        self.__resize_window_as_per_config()

    def __resize_window_as_per_config(self):
        # Resize window
        config = self.config
        browser_width = config.setu_config.value(SetuConfigOption.BROWSER_DIM_WIDTH)
        browser_height = config.setu_config.value(SetuConfigOption.BROWSER_DIM_HEIGHT)
        should_maximize = config.setu_config.value(SetuConfigOption.BROWSER_MAXIMIZE)

        if config.setu_config.is_not_set(SetuConfigOption.BROWSER_DIM_WIDTH) and config.setu_config.is_not_set(SetuConfigOption.BROWSER_DIM_HEIGHT):
            if should_maximize:
                self.maximize()
        else:
            width, height = None, None
            current_width, current_height = self.get_size()
            width = config.setu_config.is_not_set(SetuConfigOption.BROWSER_DIM_WIDTH) and browser_width or current_width
            height = config.setu_config.is_not_set(SetuConfigOption.BROWSER_DIM_HEIGHT) and browser_height or current_height
            self.set_window_size(width, height)

    def is_main_window(self):
        return True

    def close(self):
        raise Exception("You can not close main window. Use automator.quit() to quit application.")

class ChildWindow(BasicWindow):

    def __init__(self, automator, handle):
        super().__init__(automator)
        self._set_handle(handle) 

    def close(self):
        self._act(TestAutomatorActionBodyCreator.close_current_window())
        self.automator.window_handler.delete_window(self.setu_id, self.handle)
        self.automator.window_handler.jump_to_main_window()
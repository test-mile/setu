from setu.core.config.config_utils import Config
from setu.core.guiauto.actions.automator_actions import \
    TestAutomatorActionBodyCreator

from .guiautomator import GuiAutomator
from .handler import Handler

class WindowHandler(Handler):

    def __init__(self, automator: GuiAutomator):
        super().__init__(automator)
        self._main_win_handle = self.get_current_window_handle()
        from setu.core.guiauto.element.window import MainWindow
        self.__main_window = MainWindow(automator, self._main_win_handle)
        self.__all_child_windows = {}
        self.__setu_id_map = {}
        self.__setu_id_map[self.__main_window.setu_id] = self.__main_window

    def get_all_child_window_handles(self):
        from setu.core.guiauto.element.window import ChildWindow
        response = self._act(TestAutomatorActionBodyCreator.get_all_window_handles())
        handles = response["data"]["handles"]
        handles = [handle for handle in handles if handle != self._main_win_handle]
        new_handles = []
        for handle in handles:
            if handle != self._main_win_handle:
                if handle not in self.__all_child_windows:
                    cwin = ChildWindow(self.automator, handle)
                    self.__all_child_windows[handle] = cwin
                    self.__setu_id_map[cwin.setu_id] = cwin
                    new_handles.append(handle)
        return handles, new_handles

    def create_new_child_window(self):
        _, new_handles = self.get_all_child_window_handles()
        if not new_handles:
            raise Exception("No new window was launched.")
        elif len(new_handles) > 1:
            raise Exception("Multiple new windows were launched, so can not deterministically jump to a new window.")
        return self.__all_child_windows[new_handles[0]]

    def __get_child_window(self, handle):
        return self.__all_child_windows[handle]

    def __jump_to_window(self, handle):
        self.__get_child_window(handle).jump()

    def jump_to_main_window(self):
        self.__main_window.jump()

    def delete_window(self, setu_id, handle):
        del self.__all_child_windows[handle]
        del self.__setu_id_map[setu_id]

    def close_all_child_windows(self):
        all_child_handles, _ = self.get_all_child_window_handles()
        for handle in all_child_handles:
            cwin = self.__get_child_window(handle)
            cwin.jump()
            cwin.close()
        self.jump_to_main_window()

    def get_current_window_handle(self):
        response = self._act(TestAutomatorActionBodyCreator.get_current_window_handle())
        return response["data"]["handle"]

    def get_main_window(self):
        return self.__main_window

    def get_window_for_setu_id(self, setu_id):
        return self.__setu_id_map[setu_id]

    def get_window_for_locator(self, locator_type, locator_value):
        all_child_handles, _ = self.get_all_child_window_handles()
        for handle in all_child_handles:
            cwin = self.__get_child_window(handle)
            cwin.jump()    
            if locator_type.lower() == "window_title":
                if cwin.get_title() == locator_value:
                    return cwin
                else:
                    try:
                        element = self.automator.create_element_with_locator(locator_type, locator_value)
                        element.find()
                        return cwin
                    except:
                        continue
        raise Exception("No child window contains an element with locator type: {} and locator value: {}".format(locator_type, locator_value))



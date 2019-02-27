import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig

from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

win_handler = automator.window_handler
print(win_handler.get_current_window_handle())
print(win_handler.get_current_window_size())
print(win_handler.get_all_window_handles())
win_handler.set_window_size(200,400)
time.sleep(5)
win_handler.maximize_window()
time.sleep(5)
print(win_handler.get_window_title())
automator.execute_javascript("window.open('google.com')")
print(win_handler.get_all_window_handles())
print(win_handler.get_window_title())
time.sleep(5)
win_handler.switch_to_new_window()
print(win_handler.get_window_title())
win_handler.close_current_window()
time.sleep(5)
automator.execute_javascript("window.open('google.com')")
print(win_handler.get_all_window_handles())
time.sleep(5)
automator.execute_javascript("window.open('yahoo.com')")
print(win_handler.get_all_window_handles())
time.sleep(5)
automator.execute_javascript("window.open('bing.com')")
print(win_handler.get_all_window_handles())
time.sleep(5)
win_handler.close_all_child_windows()
print(win_handler.get_window_title())
time.sleep(5)
win_handler.close_current_window()

logout(automator)
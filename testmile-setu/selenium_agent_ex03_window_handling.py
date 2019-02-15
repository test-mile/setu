import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig

#####################
# Creating Gui Automator
#####################

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
automator.launch()

#####################
# Basic Login Example
#####################

automator.go_to("http://192.168.56.103/wp-admin")

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

#automator.go_to("http://192.168.56.103/wp-login.php?action=logout")
#automator.quit()
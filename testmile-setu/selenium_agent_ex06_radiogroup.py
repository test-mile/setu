import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

automator.create_element_with_locator("link_text","Settings").click()
data_format = automator.create_radiogroup_with_locator("name", "date_format")
time.sleep(2)
print(data_format.has_value_selected("Y-m-d"))
time.sleep(2)
print(data_format.has_index_selected(1))
time.sleep(2)
print(data_format.get_first_selected_option_value())
time.sleep(2)
data_format.select_by_value(r'\c\u\s\t\o\m')
time.sleep(2)
data_format.select_by_index(2)

logout(automator)
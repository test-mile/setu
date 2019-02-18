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

automator.browser_navigator.to("http://192.168.56.103/wp-admin")
automator.create_element_with_locator("id","user_login").set_text("user")
automator.create_element_with_locator("id","user_pass").set_text("bitnami")
automator.create_element_with_locator("id","wp-submit").click()
automator.create_element_with_locator("class_name","welcome-view-site").wait_until_clickable()

#####################
# Radio Group
#####################

automator.create_element_with_locator("link_text","Settings").click()
data_format = automator.convert_to_radiogroup(automator.create_multielement_with_locator("name", "date_format"))
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

#automator.go_to("http://192.168.56.103/wp-login.php?action=logout")
#automator.quit()
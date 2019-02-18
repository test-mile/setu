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

automator.create_element_with_locator("link_text","Settings").click()
role_select = automator.convert_to_select(automator.create_element_with_locator("id","default_role"))
print(role_select.has_visible_text_selected("Subscriber"))
print(role_select.has_value_selected("subscriber"))
print(role_select.has_index_selected(2))
print(role_select.get_first_selected_option())
role_select.select_by_value("editor")
role_select.select_by_visible_text("Subscriber")
role_select.select_by_index(4)

#automator.go_to("http://192.168.56.103/wp-login.php?action=logout")
#automator.quit()
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
automator.create_element_with_locator("id","user_login").set_text("user")
automator.create_element_with_locator("id","user_pass").set_text("bitnami")
automator.create_element_with_locator("id","wp-submit").click()
automator.create_element_with_locator("class_name","welcome-view-site").wait_until_clickable()

automator.take_screenshot()

automator.create_element_with_locator("link_text","Posts").click()
automator.create_element_with_locator("link_text","Categories").click()
checkboxes = automator.create_multielement_with_locator("name","delete_tags[]")
checkboxes.get_instance_at_index(0).check()
checkboxes.get_instance_at_index(0).uncheck()
checkboxes.get_instance_at_index(0).check()
# Should not change the state
checkboxes.get_instance_at_index(0).check()
checkboxes.get_instance_at_index(1).check()

#automator.go_to("http://192.168.56.103/wp-login.php?action=logout")
#automator.quit()
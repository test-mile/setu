import time

from setu import GuiAutomator
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig

#####################
# Creating Gui Automator
#####################

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))

def login(automator):
    automator.launch()

    automator.browser_navigator.to("http://192.168.56.103/wp-admin")
    automator.create_element_with_locator("id","user_login").set_text("user")
    automator.create_element_with_locator("id","user_pass").set_text("bitnami")
    automator.create_element_with_locator("id","wp-submit").click()
    automator.create_element_with_locator("class_name","welcome-view-site").wait_until_clickable()

def logout(automator):
    automator.browser_navigator.to("http://192.168.56.103/wp-login.php?action=logout")
    automator.quit()
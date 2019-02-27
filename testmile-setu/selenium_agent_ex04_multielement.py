import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig

from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

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

logout(automator)
import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

automator.create_element_with_locator("link_text","Settings").click()
role_select = automator.create_dropdown("id","default_role")
print(role_select.has_visible_text_selected("Subscriber"))
print(role_select.has_value_selected("subscriber"))
print(role_select.has_index_selected(2))
print(role_select.get_first_selected_option_text())
role_select.select_by_value("editor")
role_select.select_by_visible_text("Subscriber")
role_select.select_by_index(4)

logout(automator)
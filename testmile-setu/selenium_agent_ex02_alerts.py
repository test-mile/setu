import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

alert_handler = automator.alert_handler
automator.execute_javascript("alert('dummy')")
alert_handler.confirm_alert()
automator.execute_javascript("alert('dummy')")
alert_handler.dismiss_alert()
automator.execute_javascript("alert('Sample')")
assert alert_handler.get_text_from_alert() == "Sample"
alert_handler.confirm_alert()
time.sleep(3)
automator.execute_javascript("prompt('Are You Sure?')")
alert_handler.send_text_to_alert("Yes")
alert_handler.dismiss_alert()

logout(automator)

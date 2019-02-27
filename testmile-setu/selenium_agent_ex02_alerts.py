import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

alert_handler = automator.alert_handler
automator.execute_javascript("alert('dummy')")
alert_handler.create_alert().confirm()
automator.execute_javascript("alert('dummy')")
alert_handler.create_alert().dismiss()

automator.execute_javascript("alert('Sample')")
alert = alert_handler.create_alert()
assert alert.get_text() == "Sample"
alert.confirm()
time.sleep(3)

automator.execute_javascript("prompt('Are You Sure?')")
alert = alert_handler.create_alert()
alert.send_text("Yes")
alert.confirm()
time.sleep(3)

logout(automator)

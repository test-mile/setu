import time

from setu import GuiAutomator
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)
logout(automator)
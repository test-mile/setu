import time

from setu import GuiAutomator
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from setu.core.guiauto.gui.mgr import GuiManager

#####################
# Creating Gui Automator
#####################

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))



#automator.quit()
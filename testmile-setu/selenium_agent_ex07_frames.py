import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.config.ex import EX_CONFIG
from setu.core.config.config_utils import SetuConfig
from wp_login_logout import login, logout

automator = GuiAutomator("http://localhost:9898", SetuConfig(EX_CONFIG))
login(automator)

automator.create_element_with_locator("link_text","Posts").click()
automator.create_element_with_locator("link_text","Add New").click()

automator.create_element_with_locator("id","title").set_text("Sample")

# jump to frame by name
frame = automator.create_frame_with_locator("id", "content_ifr")
frame.jump()
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - frame by name.")
frame.jump_to_root()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)
# jump to frame by index
frame = automator.create_frame_with_locator("index", "0")
frame.jump()
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - frame by index.")
frame.jump_to_root()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)
# jump to parent
frame = automator.create_frame_with_locator("xpath", "//iframe")
frame.jump()
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - jumping to parent after this.")
frame.jump_to_parent()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)

logout(automator)
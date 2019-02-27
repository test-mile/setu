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

frame_handler = automator.frame_handler
# Switch to frame by name
frame_handler.switch_to_frame_by_name("content_ifr")
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - frame by name.")
frame_handler.switch_to_root()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)
# Switch to frame by name
frame_handler.switch_to_frame_by_index(0)
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - frame by index.")
frame_handler.switch_to_root()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)
# Switch to frame by element, use GuiElement representing the frame
frame_element = automator.create_element_with_locator("id", "content_ifr")
frame_handler.switch_to_frame_of_element(frame_element)
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - frame of element.")
frame_handler.switch_to_root()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)
# Switch to parent
frame_element = automator.create_element_with_locator("xpath", "//iframe")
frame_handler.switch_to_frame_of_element(frame_element)
tiny_mce = automator.create_element_with_locator("id","tinymce")
tiny_mce.set_text("This is a test - switching to parent after this.")
frame_handler.switch_to_parent_frame()
automator.create_element_with_locator("id","publish").click()
time.sleep(5)

logout(automator)
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

#####################
# Take screenshot
#####################
# automator.take_screenshot()

#####################
# Window Handling
#####################

# win_handler = automator.window_handler
# print(win_handler.get_current_window_handle())
# print(win_handler.get_current_window_size())
# print(win_handler.get_all_window_handles())
# win_handler.set_window_size(200,400)
# time.sleep(5)
# win_handler.maximize_window()
# time.sleep(5)
# print(win_handler.get_window_title())
# automator.execute_javascript("window.open('google.com')")
# print(win_handler.get_all_window_handles())
# print(win_handler.get_window_title())
# time.sleep(5)
# win_handler.switch_to_new_window()
# print(win_handler.get_window_title())
# win_handler.close_current_window()
# time.sleep(5)
# automator.execute_javascript("window.open('google.com')")
# print(win_handler.get_all_window_handles())
# time.sleep(5)
# automator.execute_javascript("window.open('yahoo.com')")
# print(win_handler.get_all_window_handles())
# time.sleep(5)
# automator.execute_javascript("window.open('bing.com')")
# print(win_handler.get_all_window_handles())
# time.sleep(5)
# win_handler.close_all_child_windows()
# print(win_handler.get_window_title())
# time.sleep(5)
# win_handler.close_current_window()

#####################
# Multi-Element
#####################

# automator.create_element_with_locator("link_text","Posts").click()
# automator.create_element_with_locator("link_text","Categories").click()
# checkboxes = automator.create_multielement_with_locator("name","delete_tags[]")
# checkboxes.get_instance_at_index(0).check()
# checkboxes.get_instance_at_index(0).uncheck()
# checkboxes.get_instance_at_index(0).check()
# # Should not change the state
# checkboxes.get_instance_at_index(0).check()

#####################
# Set/Enter Text
#####################

# automator.create_element_with_locator("link_text","Settings").click()
# blog_name = automator.create_element_with_locator("id", "blogname")
# blog_name.enter_text("Hello")
# blog_name.set_text("Hello")

#####################
# Select
#####################
# automator.create_element_with_locator("link_text","Settings").click()
# role_select = automator.convert_to_select(automator.create_element_with_locator("id","default_role"))
# time.sleep(2)
# print(role_select.has_visible_text_selected("Subscriber"))
# time.sleep(2)
# print(role_select.has_value_selected("subscriber"))
# time.sleep(2)
# print(role_select.has_index_selected(2))
# time.sleep(2)
# print(role_select.get_first_selected_option())
# time.sleep(2)
# role_select.select_by_value("editor")
# time.sleep(2)
# role_select.select_by_visible_text("Subscriber")
# time.sleep(2)
# role_select.select_by_index(4)
# time.sleep(5)

#####################
# Radio Group
#####################

# automator.create_element_with_locator("link_text","Settings").click()
# data_format = automator.convert_to_radiogroup(automator.create_multielement_with_locator("name", "date_format"))
# time.sleep(2)
# print(data_format.has_value_selected("Y-m-d"))
# time.sleep(2)
# print(data_format.has_index_selected(1))
# time.sleep(2)
# print(data_format.get_first_selected_option())
# time.sleep(2)
# data_format.select_by_value(r'\c\u\s\t\o\m')
# time.sleep(2)
# data_format.select_by_index(2)

#####################
# Frame Handling
#####################

# automator.create_element_with_locator("link_text","Posts").click()
# automator.create_element_with_locator("link_text","Add New").click()
# automator.create_element_with_locator("id","title").set_text("Sample")

# frame_handler = automator.frame_handler
# # Switch to frame by name
# frame_handler.switch_to_frame_by_name("content_ifr")
# tiny_mce = automator.create_element_with_locator("id","tinymce")
# tiny_mce.set_text("This is a test - frame by name.")
# frame_handler.switch_to_root()
# automator.create_element_with_locator("id","publish").click()
# time.sleep(5)
# # Switch to frame by name
# frame_handler.switch_to_frame_by_index(0)
# tiny_mce = automator.create_element_with_locator("id","tinymce")
# tiny_mce.set_text("This is a test - frame by index.")
# frame_handler.switch_to_root()
# automator.create_element_with_locator("id","publish").click()
# time.sleep(5)
# # Switch to frame by element, use GuiElement representing the frame
# frame_element = automator.create_element_with_locator("id", "content_ifr")
# frame_handler.switch_to_frame_of_element(frame_element)
# tiny_mce = automator.create_element_with_locator("id","tinymce")
# tiny_mce.set_text("This is a test - frame of element.")
# frame_handler.switch_to_root()
# automator.create_element_with_locator("id","publish").click()
# time.sleep(5)
# # Switch to parent
# frame_element = automator.create_element_with_locator("xpath", "//iframe")
# frame_handler.switch_to_frame_of_element(frame_element)
# tiny_mce = automator.create_element_with_locator("id","tinymce")
# tiny_mce.set_text("This is a test - switching to parent after this.")
# frame_handler.switch_to_parent_frame()
# automator.create_element_with_locator("id","publish").click()
# time.sleep(5)

######################
# Context
######################



#automator.go_to("http://192.168.56.103/wp-login.php?action=logout")
#automator.quit()
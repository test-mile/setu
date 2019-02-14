import time

from setu import GuiAutomator, SimpleGuiElementMetaData
from setu.core.guiauto.config import ex

automator = GuiAutomator("http://localhost:9898", ex)
automator.launch()

automator.go_to("http://192.168.56.103/wp-admin")
automator.create_element_with_locator("id","user_login").set_text("user")
automator.create_element_with_locator("id","user_pass").set_text("bitnami")
automator.create_element_with_locator("id","wp-submit").click()
automator.create_element_with_locator("class_name","welcome-view-site").wait_until_clickable()

# automator.create_element_with_locator("link_text","Posts").click()
# automator.create_element_with_locator("link_text","Categories").click()
# checkboxes = automator.create_multielement_with_locator("name","delete_tags[]")
# checkboxes.get_instance_at_index(0).check()
# checkboxes.get_instance_at_index(0).uncheck()
# checkboxes.get_instance_at_index(0).check()
# # Should not change the state
# checkboxes.get_instance_at_index(0).check()

automator.create_element_with_locator("link_text","Settings").click()
blog_name = automator.create_element_with_locator("id", "blogname")
blog_name.enter_text("Hello")
blog_name.set_text("Hello")
role_select = automator.convert_to_select(automator.create_element_with_locator("id","default_role"))
print(role_select.is_visible_text_selected("Subscriber"))
print(role_select.is_value_selected("subscriber"))
print(role_select.is_index_selected(2))
print(role_select.get_first_selected_option())
role_select.select_by_value("editor")
role_select.select_by_visible_text("Subscriber")
#automator.quit()

'''
		
		automator.getElementFinder().find("id", "users_can_register").getCheckBoxHandler().check();
		
		DropdownHandler roleDropDown = automator.getElementFinder().find("id", "default_role").asDropDown();

		roleDropDown.selectText("Author");
		assertTrue(roleDropDown.hasSelectedText("Author"), "Check Author Role Selected");
		roleDropDown.selectAtIndex(0);
		assertTrue(roleDropDown.hasSelectedIndex(0), "Check Author Role Selected");
		roleDropDown.selectValue("author");
		assertTrue(roleDropDown.hasSelectedValue("author"), "Check Author Role Selected");
		
		automator.getBrowserHandler().goTo("http://192.168.56.103/wp-login.php?action=logout");
		
		automator.quit();
'''

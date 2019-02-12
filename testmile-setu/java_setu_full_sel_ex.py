import requests
import uuid

from config import ex
from automator_actions import *

class SetuAgentRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url):
        response = requests.get(self.base_url + url)
        print(response.text)

    def post(self, url, json_dict):
        response = requests.post(self.base_url + url, json=json_dict)
        print(response.text)

class SetuManagedObject:

    def __init__(self):
        self.setu_id = str(uuid.uuid4())

    def get_setu_id(self):
        return self.setu_id

class GuiAutomator(SetuManagedObject):

    def __init__(self, agent_base_url, config_dict):
        super().__init__()
        self.agent_base_url = agent_base_url
        self.automator_uri = "/guiauto/automator/{}".format(self.setu_id)
        self.config_dict = config_dict
        self.requester = SetuAgentRequester(self.agent_base_url)
        self.element_map = {}

    def get_agent_base_url(self):
        return self.agent_base_url

    def get_agent_requester(self):
        return self.requester

    def __get_full_uri(self, suffix):
        return self.automator_uri + suffix

    def __action(self, json_dict):
        self.requester.post(self.__get_full_uri("/action"), json_dict)

    def create_element(self, emd):
        element = GuiElement(self, emd)
        self.element_map[element.get_setu_id()] = element
        return element

    def launch(self):
        self.requester.post(self.__get_full_uri("/launch"), self.config_dict)

    def go_to(self, url):
        self.__action(TestAutomatorActionBodyCreator.goTo(url=url))

    def find_element(self, gui_element):
        print(gui_element.get_locator_meta_data().get_locators())
        for locator_type, locator_value in gui_element.get_locator_meta_data().get_locators(): 
            try:
                self.__action(TestAutomatorActionBodyCreator.find(
                    uuid=gui_element.get_setu_id(),
                    byType=locator_type,
                    byValue=locator_value
                ))
                gui_element.set_found_with(locator_type, locator_value)
                break
            except:
                continue

class GuiElement(SetuManagedObject):
    
    def __init__(self, automator, emd):
        super().__init__()
        self.automator = automator
        self.emd = emd
        self.found = False
        self.element_base_uri = "/guiauto/element/{}".format(self.setu_id)
        self.requester = self.automator.get_agent_requester()
        self.located_by = None

    def __get_full_uri(self, suffix):
        return self.element_base_uri + suffix

    def __action(self, json_dict):
        self.requester.post(self.__get_full_uri("/action"), json_dict)

    def get_locator_meta_data(self):
        return self.emd

    def is_found(self):
        return self.found

    def set_found_with(self, locator_type, locator_value):
        self.found = True
        self.located_by = locator_type, locator_value

    def clear_text(self):
        self.__action(ElementActionBodyCreator.clearText())

    def enter_text(self, text):
        self.__action(ElementActionBodyCreator.enterText(text=text))

    def __find_if_not_found(self):
        if not self.found:
            self.automator.find_element(self)

    def set_text(self, text):
        self.__find_if_not_found()
        self.clear_text()
        self.enter_text(text)

    def click(self):
        self.__find_if_not_found()
        self.__action(ElementActionBodyCreator.click())

    def wait_until_clickable(self):
        self.__find_if_not_found()
        self.__action(ElementActionBodyCreator.wait_until_clickable())

class GuiElementMetaData:

    def __init__(self, locator_dict):
        self.locator_dict = locator_dict

    def get_locators(self): # needs platform info. Then returns platform-specfic + common loctors.
        return (self.locator_dict["common"],)

class SimpleGuiElementMetaData(GuiElementMetaData):

    def __init__(self, locator_type, locator_value):
        super().__init__({"common" : (locator_type, locator_value)})

########################
#     Usage Code
########################

automator = GuiAutomator("http://localhost:9898", ex)
automator.launch()
automator.go_to("http://192.168.56.103/wp-admin")
user_text_box = automator.create_element(SimpleGuiElementMetaData("id","user_login"))
user_text_box.set_text("user")
password_box = automator.create_element(SimpleGuiElementMetaData("id","user_pass"))
password_box.set_text("bitnami")
submit_button = automator.create_element(SimpleGuiElementMetaData("id","wp-submit"))
submit_button.click()
view_site_link = automator.create_element(SimpleGuiElementMetaData("class_name","welcome-view-site"))
view_site_link.wait_until_clickable()

# response = requests.get(agent_base_url + "/guiauto/automator/{}/quit".format(automator_uuid))
# print(response.text)

'''	
		// Wait
		automator.getElementFinder().find("class_name", "welcome-view-site").getStateHandler().waitUntilClickable();
		
		automator.getElementFinder().find("link_text", "Posts").getBasicActionsHandler().click();
		automator.getElementFinder().find("link_text", "Categories").getBasicActionsHandler().click();
		
		GuiMultiElement checkboxes = automator.getElementFinder().findAll("name", "delete_tags[]");
		checkboxes.getInstanceAtIndex(0).getCheckBoxHandler().check();
		checkboxes.getInstanceAtIndex(0).getCheckBoxHandler().uncheck();

		automator.getElementFinder().find("link_text", "Settings").getBasicActionsHandler().click();
		GuiElement blogName = automator.getElementFinder().find("id", "blogname");
		blogName.getBasicActionsHandler().enterText("Hello");
		blogName.getBasicActionsHandler().enterText("Hello");
		blogName.getBasicActionsHandler().setText("Hello");
		
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
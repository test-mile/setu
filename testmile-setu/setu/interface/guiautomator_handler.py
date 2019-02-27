import uuid
from setu.core.guiauto.automator.guiautomator import GuiAutomator
from setu.core.config.config_utils import SetuConfig
from .element_handlers import *


# Arg names of methods show JSON names, so don't follow Python conventions.
class GuiAutomatorHandler:

    def __init__(self):
        self.__automator = None

    @property
    def setu_id(self):
        return self.automator.setu_id

    @property
    def automator(self):
        return self.__automator

    def launch_automator(self, config):
        automator = GuiAutomator("http://localhost:9898", SetuConfig(config))
        automator.launch()
        self.__automator = automator

    def quit(self):
        self.automator.quit()

    def navigate_browser(self, navType, url=None):
        ntype = navType.lower()
        if ntype == "to":
            getattr(self.automator.browser_navigator, ntype)(url)
        else:
            getattr(self.automator.browser_navigator, ntype)()

    def create_element(self, withType, withValue):
        elem = self.automator.create_element_with_locator(withType, withValue)
        return {"elementSetuId" : elem.setu_id}

    def create_multielement(self, withType, withValue):
        elem = self.automator.create_multielement_with_locator(withType, withValue)
        return {"elementSetuId" : elem.setu_id}

    def create_dropdown(self, withType, withValue):
        dropdown = self.automator.create_dropdown_with_locator(withType, withValue)
        return {"elementSetuId" : dropdown.setu_id}

    def create_radiogroup(self, withType, withValue):
        radiogroup = self.automator.create_radiogroup_with_locator(withType, withValue)
        return {"elementSetuId" : radiogroup.setu_id}

    def create_frame(self, withType, withValue):
        radiogroup = self.automator.create_frame_with_locator(withType, withValue)
        return {"elementSetuId" : radiogroup.setu_id}

    def take_element_action(self, action, elem_setu_id, json_dict):
        element =  self.automator.get_element_for_setu_id(elem_setu_id)
        return getattr(ElementHandler, action)(element, **json_dict)

    def take_dropdown_action(self, action, elem_setu_id, json_dict):
        dropdown =  self.automator.get_element_for_setu_id(elem_setu_id)
        return getattr(DropdownHandler, action)(dropdown, **json_dict)

    def take_radiogroup_action(self, action, elem_setu_id, json_dict):
        radiogroup =  self.automator.get_element_for_setu_id(elem_setu_id)
        return getattr(RadioGroupHandler, action)(radiogroup, **json_dict)

    def take_frame_action(self, action, elem_setu_id, json_dict):
        frame =  self.automator.get_element_for_setu_id(elem_setu_id)
        return getattr(FrameHandler, action)(frame, **json_dict)

    def take_window_action(self, action, elem_setu_id, json_dict):
        win =  self.automator.window_handler.get_window_for_setu_id(elem_setu_id)
        return getattr(WindowHandler, action)(win, **json_dict)

    def take_multielement_action(self, action, elem_setu_id, json_dict):
        multi_element =  self.automator.get_multielement_for_setu_id(elem_setu_id)
        is_instance_action = json_dict["isInstanceAction"]
        del json_dict["isInstanceAction"]
        if is_instance_action:
            index = json_dict["instanceIndex"]
            del json_dict["instanceIndex"]
            element = multi_element.get_instance_at_index(index)
            return getattr(ElementHandler, action)(element, **json_dict)
        else:
            return getattr(MultiElementHandler, action)(element, **json_dict)

    def execute_javascript(self, script):
        self.automator.execute_javascript(script)

    def handle_alert(self, handleType, text=None):
        handle_type = handleType.lower()
        if handle_type == "send_text_to_alert":
            return getattr(self.automator.alert_handler, handle_type)(text)
        elif handle_type == "get_text_from_alert":
            return {"text" : getattr(self.automator.alert_handler, handle_type)()}
        else:
            return getattr(self.automator.alert_handler, handle_type)()   

    def __handle_windows(self, handleType):
        handle_type = handleType.lower()
        return getattr(self.automator.window_handler, handle_type)()  

    def get_main_window(self):
        return {"elementSetuId" : self.__handle_windows("get_main_window").setu_id}

    def close_all_child_windows(self):
        return self.__handle_windows("close_all_child_windows")  

    def create_new_child_window(self):
        return {"elementSetuId" : self.__handle_windows("create_new_child_window").setu_id}
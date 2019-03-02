from setu.core.test.testsession import TestSession
from .guiautomator_handler import GuiAutomatorHandler

class TestSessionHandler:

    def __init__(self):
        self.__testsession = None
        self.__automator_handlers = {}

    def __register_gui_automator_handler(self, handler):
        self.__automator_handlers[handler.setu_id] = handler

    def __deregister_gui_automator_handler(self, handler):
        del self.__automator_handlers[handler.setu_id]

    def __get_gui_automator_handler(self, setu_id):
        return self.__automator_handlers[setu_id]

    @property
    def setu_id(self):
        return self.__testsession.setu_id

    def init(self, root_dir):
        self.__testsession = TestSession()
        return self.__testsession.init(root_dir)

    def load_project_conf(self):
        return {"configSetuId" : self.__testsession.load_project_conf()}

    def get_automator_handler(self, json_dict):
        handler = self.__get_gui_automator_handler(json_dict["args"]["automatorSetuId"])
        del json_dict["args"]["automatorSetuId"]
        return handler

    def launch_automator(self, json_dict):
        config_setu_id = json_dict["args"]["configSetuId"]
        del json_dict["args"]["configSetuId"]
        config = self.__testsession.configurator.get_config(config_setu_id)
        handler = GuiAutomatorHandler()
        handler.launch_automator(config)
        self.__register_gui_automator_handler(handler)
        return {'automatorSetuId' : handler.setu_id}

    def quit_automator(self, json_dict):
        auto_handler = self.get_automator_handler(json_dict)
        auto_handler.quit()
        self.__deregister_gui_automator_handler(auto_handler) 

    def take_automator_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        return getattr(handler, json_dict["action"].lower())(**json_dict["args"])

    def take_element_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_element_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def take_multielement_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_multielement_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def take_dropdown_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_dropdown_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def take_radiogroup_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_radiogroup_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def take_frame_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_frame_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def take_window_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_window_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def take_alert_action(self, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_alert_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])

    def get_setu_option_value(self, configSetuId, option):
        return {"value" : self.__testsession.configurator.get_setu_option_value(configSetuId, option)}

    def register_config(self, setuOptions, userOptions=None):
        return {"configSetuId" : self.__testsession.configurator.register_config(setuOptions, userOptions)}


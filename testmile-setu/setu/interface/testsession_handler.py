from setu.core.test.testsession import TestSession
from .guiautomator_handler import GuiAutomatorHandler
from .conf_handler import TestSessionConfHandler
from .databroker_handler import TestSessionDataBrokerHandler
from setu.core.constants import SetuConfigOption

class TestSessionHandler:

    def __init__(self):
        self.__testsession = None
        self.__automator_handlers = {}
        self.__conf_handler = None
        self.__databroker_handler = None


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
        conf = self.__testsession.init(root_dir)
        self.__conf_handler = TestSessionConfHandler(self.__testsession.configurator)
        self.__databroker_handler = TestSessionDataBrokerHandler(self.__testsession.data_broker)
        return conf

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

    def take_conf_action(self, json_dict):
        return getattr(self.__conf_handler, json_dict["action"].lower())(**json_dict["args"])    

    def take_datasource_action(self, json_dict):
        return getattr(self.__databroker_handler, json_dict["action"].lower())(**json_dict["args"]) 

    def register_config(self, setuOptions, hasParent, userOptions=None, parentConfigId=None):
        return {"configSetuId" : self.__testsession.configurator.register_config(setuOptions, hasParent, userOptions, parentConfigId)}

    def load_project_conf(self):
        return {"configSetuId" : self.__testsession.configurator.create_project_conf()}  

    def create_file_data_source(self, fileName, recordType, **kwargs):
        data_dir = self.__testsession.configurator.get_central_setu_option_value(SetuConfigOption.DATA_SOURCES_DIR.name)
        return {"dataSourceSetuId" : self.__testsession.data_broker.create_file_data_source(data_dir, fileName, recordType, **kwargs)}  

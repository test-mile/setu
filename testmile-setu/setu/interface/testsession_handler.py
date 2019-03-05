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

    def get_element_setuid(self, json_dict):
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return elem_setu_id

    def take_session_action(self, action, json_dict):
        print(json_dict)
        return getattr(self, action)(json_dict)

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

    def take_automator_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        return getattr(handler, action)(**json_dict["args"])

    def take_element_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = self.get_element_setuid(json_dict)
        return handler.take_element_action(action, elem_setu_id, json_dict["args"])

    def take_browser_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        return handler.take_browser_action(action, json_dict["args"])

    def take_multielement_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_multielement_action(action, elem_setu_id, json_dict["args"])

    def take_dropdown_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_dropdown_action(action, elem_setu_id, json_dict["args"])

    def take_radiogroup_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_radiogroup_action(action, elem_setu_id, json_dict["args"])

    def take_frame_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_frame_action(action, elem_setu_id, json_dict["args"])

    def take_window_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_window_action(action, elem_setu_id, json_dict["args"])

    def take_main_window_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_window_action(action, elem_setu_id, json_dict["args"])

    def take_child_window_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_window_action(action, elem_setu_id, json_dict["args"])

    def take_alert_action(self, action, json_dict):
        handler = self.get_automator_handler(json_dict)
        elem_setu_id = json_dict["args"]["elementSetuId"]
        del json_dict["args"]["elementSetuId"]
        return handler.take_alert_action(action, elem_setu_id, json_dict["args"])

    def take_conf_action(self, action, json_dict):
        return getattr(self.__conf_handler, action)(**json_dict["args"])    

    def take_datasource_action(self, action, json_dict):
        return getattr(self.__databroker_handler, action)(**json_dict["args"]) 

    def register_config(self, json_dict):
        setu_options = self.return_and_remove_arg(json_dict, 'setuOptions')
        has_parent = self.return_and_remove_arg(json_dict, 'hasParent')
        user_options = self.return_and_remove_arg(json_dict, 'userOptions', optional=True)
        parent_config_id = self.return_and_remove_arg(json_dict, 'parentConfigId', optional=True)
        return {"configSetuId" : self.__testsession.configurator.register_config(setu_options, has_parent, user_options, parent_config_id)}

    def load_project_conf(self, json_dict):
        return {"configSetuId" : self.__testsession.configurator.create_project_conf()}  

    def return_and_remove_arg(self, json_dict, key, optional=False):
        try:
            value = json_dict['args'][key]
            del json_dict['args'][key]
            return value
        except:
            if optional: 
                return None
            else: raise Exception("Input value for {} not found in JSON {}.".format(key, json_dict))

    def create_file_data_source(self, json_dict):
        file_name = self.return_and_remove_arg(json_dict, 'fileName')
        record_type = self.return_and_remove_arg(json_dict, 'recordType')
        data_dir = self.__testsession.configurator.get_central_setu_option_value(SetuConfigOption.DATA_SOURCES_DIR.name)
        return {"dataSourceSetuId" : self.__testsession.data_broker.create_file_data_source(data_dir, file_name, record_type, **json_dict['args'])}  

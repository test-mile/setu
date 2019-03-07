import inspect

class GuiAutomator:

    def __init__(self, setu_id, requester):
        self.__setu_id = setu_id
        self.__requester = requester

    def post(self, **kwargs):
        input_dict = {"automatorSetuId" : self.setu_id}
        input_dict.update(kwargs)
        json_dict = {
            "action" : inspect.stack()[1].function,
            "args" : input_dict
        }
        return self.__requester.post("/guiautomator", json_dict)

    @property
    def setu_id(self):
        return self.__setu_id

    def launch(self, config):
        self.post(config=config)

    def quit(self):
        self.post()

    def go_to_url(self, url):
        print("gggg", url)
        self.post(url=url)

    def go_back_in_browser(self):
        self.post()

    def go_forward_in_browser(self):
        self.post()

    def refersh_browser(self):
        self.post()

    def execute_javascript(self, script):
        self.post(script=script)

    def take_screenshot(self):
        self.post()

    def find_element(self, child_gui_element_set_id, with_type, with_value):
        self.post(
            elementSetuId = child_gui_element_set_id,
            withType = with_type,
            withValue = with_value
        )

    def find_multielement(self, child_gui_element_set_id, with_type, with_value):
        response = self.post(
            elementSetuId = child_gui_element_set_id,
            withType = with_type,
            withValue = with_value
        )

        return response["data"]["instanceCount"]

    def __get_value_from_response(self, response, key):
        if "data" not in response:
            raise Exception("Setu actor json response: {} does not contain 'data' key.")
        elif key not in response:
            raise Exception("Setu actor json response: {} does not contain key <{}> in data section.")
        else:
            return response["data"][key]

    def __get_result(self, response):
        return self.__get_value_from_response(response, "result")

    def get_current_window_handle(self):
        response = self.post()
        print(response)
        return self.__get_result(response)

    def get_current_window_title(self):
        response = self.post()
        return self.__get_result(response)

    def maximize_current_window(self):
        self.post()

    def get_current_window_size(self):
        response = self.post()
        size = self.__get_result(response)
        return size["width"], size["height"]

    def get_all_window_handles(self):
        response = self.post()
        return self.__get_result(response)

    def focus_on_window(self, handle):
        self.post(handle=handle)

    def close_current_window(self):
        self.post()

    def is_alert_present(self):
        response = self.post()
        return self.__get_result(response)

    def confirm_alert(self):
        self.post()

    def dismiss_alert(self):
        self.post()

    def get_text_from_alert(self):
        response = self.post()
        return self.__get_result(response)

    def send_text_to_alert(self,text):
        self.post(text=text)

    def get_current_view_context(self):
        response = self.post()
        return self.__get_result(response)

    def get_all_view_contexts(self):
        response = self.post()
        return self.__get_result(response)

    def focus_on_view_context(self, view_context):
        self.post(viewContext=view_context)

    def focus_on_frame(self, elem_setu_id, is_instance_action=False, instance_index=0):
        if is_instance_action:
            self.post(elementSetuId=elem_setu_id, isInstanceAction=is_instance_action, instanceIndex=instance_index)
        else:
            self.post(elementSetuId=elem_setu_id)

    def focus_on_parent_frame(self):
        self.post()

    def focus_on_dom_root(self):
        self.post()
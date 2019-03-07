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

    def excute_javascript(self, script):
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

    def get_current_window_handle(self):
        response = self.post()
        print(response)
        return response["data"]["handle"]

    def get_current_window_title(self):
        response = self.post()
        return response["data"]["title"]

    def maximize_current_window(self):
        self.post()

    def get_current_window_size(self):
        response = self.post()
        size = response["data"]["size"]
        return size["width"], size["height"]

    def get_all_window_handles(self):
        self.post()

    def switch_to_window(self):
        self.post()

    def close_current_window(self):
        self.post()

    def is_alert_present(self):
        self.post()

    def confirm_alert(self):
        self.post()

    def dismiss_alert(self):
        self.post()

    def get_text_from_alert(self):
        self.post()

    def send_text_to_alert(self):
        self.post()

    def get_current_view_context(self):
        self.post()

    def get_all_view_contexts(self):
        self.post()

    def switch_to_view_context(self):
        self.post()

    def focus_on_frame(self, elem_setu_id, is_instance_action=False):
        self.post(elementSetuId=elem_setu_id, instanceAction=is_instance_action)

    def focus_on_parent_frame(self):
        self.post()

    def focus_on_dom_root(self):
        self.post()
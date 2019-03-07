import inspect

class GuiElement:

    def __init__(self, automator_setu_id, element_setu_id, requester):
        self.__automator_setu_id = automator_setu_id
        self.__element_set_id = element_setu_id
        self.__requester = requester
        self.__partial = False
        self.__instance_index = 0

    def set_partial(self, index):
        self.__partial = True
        self.__instance_index = index

    @property
    def automator_setu_id(self):
        return self.__automator_setu_id

    @property
    def element_setu_id(self):
        return self.__element_set_id

    @property
    def requester(self):
        return self.__requester

    def post(self, **kwargs):
        input_dict = {
            "automatorSetuId" : self.automator_setu_id,
            "elementSetuId" : self.element_setu_id
        }

        if self.__partial:
            input_dict.update( {
                "isInstanceAction" : True,
                "instanceIndex" : self.__instance_index
            })
        input_dict.update(kwargs)
        json_dict = {
            "action" : inspect.stack()[1].function,
            "args" : input_dict
        }
        return self.__requester.post("/guielement", json_dict)

    def find_element(self):
        self.post()

    def find_multielement(self):
        self.post()

    def click(self):
        self.post()

    def clear_text(self):
        self.post()

    def send_text(self, text):
        self.post(text=text)

    def is_selected(self):
        response = self.post()
        return response["data"]["result"]

    def is_visible(self):
        response = self.post()
        return response["data"]["result"]

    def is_clickable(self):
        response = self.post()
        return response["data"]["result"]

    def get_tag_name(self):
        response = self.post()
        return response["data"]["result"]

    def get_attr_value(self, attr_name):
        response = self.post(attr=attr_name)
        return response["data"]["result"]

    def get_text_content(self):
        response = self.post()
        return response["data"]["result"]
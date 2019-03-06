import inspect

class GuiElement:

    def __init__(self, automator_setu_id, requester):
        self.__automator_setu_id = automator_setu_id
        self.__requester = requester

    def post(self, element_setu_id, **kwargs):
        input_dict = {
            "automatorSetuId" : self.automator_setu_id,
            "elementSetuId" : element_setu_id
        }
        input_dict.update(kwargs)
        json_dict = {
            "action" : inspect.stack()[1].function,
            "args" : input_dict
        }
        return self.__requester.post("/guiautomator", json_dict)

    @property
    def automator_setu_id(self):
        return self.__automator_setu_id

    def find_element(self, elem_setu_id):
        self.post(elem_setu_id)

    def find_multielement(self, elem_setu_id):
        self.post(elem_setu_id)

    def click(self, elem_setu_id):
        self.post(elem_setu_id)

    def clear_text(self, elem_setu_id):
        self.post(elem_setu_id)

    def send_text(self, elem_setu_id):
        self.post(elem_setu_id)

    def is_selected(self, elem_setu_id):
        self.post(elem_setu_id)

    def is_visible(self, elem_setu_id):
        self.post(elem_setu_id)

    def is_clickable(self, elem_setu_id):
        self.post(elem_setu_id)

    def get_tag_name(self, elem_setu_id):
        self.post(elem_setu_id)

    def get_attr_value(self, elem_setu_id):
        self.post(elem_setu_id)

    def get_text_content(self, elem_setu_id):
        self.post(elem_setu_id)
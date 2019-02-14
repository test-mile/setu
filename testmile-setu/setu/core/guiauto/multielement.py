from .base_element import BaseElement
from .element import GuiElement  
from .element_actions import ElementActionBodyCreator

class GuiMultiElement(BaseElement):
    
    def __init__(self, automator, emd):
        super().__init__(automator, emd)
        self.instance_count = 0
        self.__uri = "/guiauto/multielement/{}".format(self.get_setu_id())
        self.__instances = None

    #Override
    def _get_object_uri(self):
        return self.__uri

    #Override
    def find_if_not_found(self):
        if not self.is_found():
            self.get_automator().find_multielement(self)

    def set_instance_count(self, count):
        self.instance_count = count
        self.__instances = [_GuiPartialElement(self.get_automator(), self, i) for i in range(self.instance_count)]

    def get_instance_count(self):
        return self.instance_count

    def get_instance_at_index(self, index):
        self.find_if_not_found()
        return self.__instances[index]

    def wait_until_visible(self):
        self.find_if_not_found()
        self._act(ElementActionBodyCreator.wait_until_visible())

    def __return_attr_values(self, response):
        if "data" in response and "attrValues" in response["data"]:
            return response["data"]["attrValues"]
        else:
            return None

    def get_text_contents(self):
        self.find_if_not_found()
        self.wait_until_visible()
        response = self._act(ElementActionBodyCreator.get_text_content())
        return self.__return_attr_values(response)

    def get_values(self):
        self.find_if_not_found()
        self.wait_until_visible()
        response = self._act(ElementActionBodyCreator.get_attr_value(attr="value"))
        return self.__return_attr_values(response)

    def are_selected(self):
        self.find_if_not_found()
        self.wait_until_visible()
        response = self._act(ElementActionBodyCreator.is_selected())
        return self.__return_attr_values(response)

class _GuiPartialElement(GuiElement):

    def __init__(self, automator, multi_element: GuiMultiElement, instance_number: int):
        super().__init__(automator, multi_element.get_locator_meta_data())
        self.__uri = "/guiauto/multielement/{}".format(multi_element.get_setu_id())
        self.__instance_number = instance_number

    #Override
    def _get_object_uri(self):
        return self.__uri

    #Override
    def find_if_not_found(self):
        # Unlike regular item no attempt should be made to indepently identify a part element.
        pass

    def _is_partial_element(self):
        return True

    def _get_instance_number(self):
        return self.__instance_number
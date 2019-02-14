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

    def get_instance_at_ordinal(self, ordinal):
        self.find_if_not_found()
        return self.__instances[ordinal-1]

    def get_instance_by_visible_text(self, text):
        texts = self.__get_all_texts()
        first_index = self.__find_first_text_index(texts, text)
        return self.get_instance_at_index(first_index)

    def get_instance_by_value(self, value):
        values = self.__get_all_values()
        first_index = self.__find_first_value_index(values, value)
        return self.get_instance_at_index(first_index)

    def wait_until_visible(self):
        self.find_if_not_found()
        self._act(ElementActionBodyCreator.wait_until_visible())

    def __return_attr_values(self, response):
        if "data" in response and "attrValues" in response["data"]:
            return response["data"]["attrValues"]
        else:
            return None

    def get_tag_names(self):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.get_tag_name())
        return self.__return_attr_values(response)

    def get_text_contents(self):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.get_text_content())
        return self.__return_attr_values(response)

    def get_values(self):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.get_attr_value(attr="value"))
        return self.__return_attr_values(response)

    def get_attr_values(self, attr):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.get_attr_value(attr=attr))
        return self.__return_attr_values(response)

    def are_selected(self):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.is_selected())
        return self.__return_attr_values(response)

    # getting index attribute when it does not exist retursn value attribute.
    # So, not going the Selenium way. Setu would treat index as computer counting.
    def has_index_selected(self, index):
        self.find_if_not_found()
        return self.get_instance_at_index(index).is_selected()

    # Ordinal is human counting
    def has_ordinal_selected(self, ordinal):
        return self.has_index_selected(ordinal-1)

    def __find_first_match_index(self, in_sequence, to_match):
        try:
            return in_sequence.index(to_match)
        except:
            return -1

    def __get_all_texts(self):
        self.find_if_not_found()
        texts = self.get_text_contents()
        print(texts)
        return texts

    def __find_first_text_index(self, texts, text):
        first_index = texts.index(text)
        if first_index == -1:
            raise Exception("No option with {} visible text present in drop down.".format(text))
        return first_index

    def __get_all_values(self):
        self.find_if_not_found()
        values = self.get_values()
        print(values)
        return values

    def __find_first_value_index(self, values, value):
        first_index = values.index(value)
        if first_index == -1:
            raise Exception("No option with {} value present in drop down.".format(value))
        return first_index

    def get_first_selected_instance(self):
        self.find_if_not_found()
        booleans = self.are_selected()
        print(booleans)
        first_index = None
        try:
            first_index = booleans.index(True)
        except:
            raise Exception("No option in drop down is currenlty selected.")
        else:
            return self.get_instance_at_index(first_index)

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
from setu.core.lib.setu_types import SetuManagedObject
from .element import GuiElement

# This code takes its inspiration and some re-usable code chunks from Selenium WebDriver's 
# Select Implementation in Python to provider a generic default Select solution across agents in any language.
# Reference code at: https://github.com/browserstack/selenium-webdriver-python/blob/master/selenium/webdriver/support/select.py
# Referenc code retrieved on 13 Feb, 2019.

# UUID is for client refernce. Agent does not know about this.
class GuiWebSelect(SetuManagedObject):

    def __init__(self, gui_main_element: GuiElement):
        super().__init__()
        self._wrapped_main_element = gui_main_element
        tag = self._wrapped_main_element.get_tag_name()
        if tag.lower() != "select":
            raise Exception("The element should have a 'select' tag for WebSelect element. Found: " + tag)
        self._multi = self.__is_multi_select()
        self.__options = None

    def __is_multi_select(self):
        return self._wrapped_main_element.get_attr_value("multiple") is True or self._wrapped_main_element.get_attr_value("multi") is True

    def is_multi_select(self):
        return self._multi

    def __populate_options(self):
        if not self.__options:
            self.__options = self._wrapped_main_element.create_multielement_with_locator("tag_name", "option")
            self.__options.find_if_not_found()

    # getting index attribute when it does not exist retursn value attribute.
    # So, not going the Selenium way. Setu would treat index as computer counting.
    def is_index_selected(self, index):
        self.__populate_options()
        return self.__options.get_instance_at_index(index).is_selected()

    # Ordinal is human counting
    def is_ordinal_selected(self, ordinal):
        return self.is_index_selected(ordinal-1)

    def __find_first_match_index(self, in_sequence, to_match):
        try:
            return in_sequence.index(to_match)
        except:
            return -1

    def __get_all_texts(self):
        self.__populate_options()
        texts = self.__options.get_text_contents()
        print(texts)
        return texts

    def __find_first_text_index(self, texts, text):
        first_index = texts.index(text)
        if first_index == -1:
            raise Exception("No option with {} visible text present in drop down.".format(value))
        return first_index

    def is_visible_text_selected(self, text):
        texts = self.__get_all_texts()
        first_index = self.__find_first_text_index(texts, text)
        return self.is_index_selected(first_index)

    def __get_all_values(self):
        self.__populate_options()
        values = self.__options.get_values()
        print(values)
        return values

    def __find_first_value_index(self, values, value):
        first_index = values.index(value)
        if first_index == -1:
            raise Exception("No option with {} value present in drop down.".format(value))
        return first_index

    def is_value_selected(self, value):
        values = self.__get_all_values()
        first_index = self.__find_first_value_index(values, value)
        return self.is_index_selected(first_index)

    def get_first_selected_option(self):
        self.__populate_options()
        booleans = self.__options.are_selected()
        print(booleans)
        first_index = None
        try:
            first_index = booleans.index(True)
        except:
            raise Exception("No option in drop down is currenlty selected.")
        else:
            return self.__options.get_instance_at_index(first_index)

    def select_by_index(self, index):
        if not self.is_index_selected(index):
            self.__options.get_instance_at_index(index).click()

    def select_by_ordinal(self, ordinal):
        return self.select_by_index(ordinal-1)

    def select_by_visible_text(self, text):
        texts = self.__get_all_texts()
        first_index = self.__find_first_text_index(texts, text)
        self.select_by_index(first_index)

    def select_by_value(self, value):
        values = self.__get_all_values()
        first_index = self.__find_first_value_index(values, value)
        self.select_by_index(first_index)

    # The following methods deal with multi-select and would be implemented later.

    def __validate_multi_select(self):
        if not self.is_multi_select():
            raise Exception("Deselect actions are allowed only for a multi-select dropdown.")

    def deselect_by_value(self, value):
        self.__validate_multi_select()
        values = self.__get_all_values()
        first_index = self.__find_first_value_index(values, value)
        if self.is_index_selected(first_index):
            self.__options.get_instance_at_index(first_index).click()

    def deselect_by_index(self, index):
        pass

    def deselect_by_visible_text(self, text):
        pass

    def get_selected_options(self):
        pass

    def are_visible_texts_selected(self, text_list):
        pass

    def are_values_selected(self, text_list):
        pass

    def all_options(self):
        pass

    def select_by_values(self, value_list):
        pass

    def deselect_by_values(self, value_list):
        pass

    def select_by_indices(self, indices):
        pass

    def deselect_by_indices(self, indices):
        pass

    def select_by_visible_texts(self, text_list):
        pass

    def deselect_by_visible_texts(self, text_list):
        pass
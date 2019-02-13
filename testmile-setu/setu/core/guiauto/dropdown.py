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

    def __populate_options(self):
        if not self.__options:
            self.__options = self._wrapped_main_element.create_multielement_with_locator("tag_name", "option")
            self.__options.find_if_not_found()

    def is_visible_text_selected(self, text):
        self.__populate_options()
        texts = self.__options.get_text_content()
        first_index = None
        try:
            first_index = texts.index(text)
        except:
            raise Exception("No option with {} visible text present in drop down.".format(text))
        else:
            return self.__options.get_instance_at_index(first_index).is_selected()

    def is_value_selected(self, text):
        pass

    def are_visible_texts_selected(self, text_list):
        pass

    def are_values_selected(self, text_list):
        pass

    def get_first_selected_option(self):
        pass

    def get_selected_options(self):
        pass

    def all_options(self):
        pass

    def select_by_value(self, value):
        pass

    def select_by_values(self, value_list):
        pass

    def select_by_index(self, index):
        pass

    def select_by_indices(self, indices):
        pass

    def select_by_visible_text(self, text):
        pass

    def select_by_visible_texts(self, text_list):
        pass

    def deselect_by_value(self, value):
        pass

    def deselect_by_values(self, value_list):
        pass

    def deselect_by_index(self, index):
        pass

    def deselect_by_indices(self, indices):
        pass

    def deselect_by_visible_text(self, text):
        pass

    def deselect_by_visible_texts(self, text_list):
        pass
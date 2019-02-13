from .base_element import BaseElement
from .element_actions import *
from .element_container import ElementContainer
from .emd import SimpleGuiElementMetaData

class GuiGenericElement(BaseElement):
    def __init__(self, automator, emd, uri_format):
        super().__init__(automator, emd)
        self.__element_uri = uri_format.format(self.get_setu_id())  

    #Override
    def _get_object_uri(self):
        return self.__element_uri

    #Override
    def find_if_not_found(self):
        if not self.is_found():
            self.get_automator().find_element(self)

    def _is_partial_element(self):
        return False

    def _get_instance_number(self):
        raise Exception("Instance number is applicable only for partial gui elements.")

    def __append_instance_number(self, d):
        if self._is_partial_element():
            d["isInstanceAction"] = True
            d["instanceIndex"] = self._get_instance_number()
        return d

    def _kwargs(self, **kwargs):
        return self.__append_instance_number(kwargs)

    def _noargs(self):
        return self.__append_instance_number({})

    def _only_send_text(self, text):
        self._act(ElementActionBodyCreator.send_text(**self._kwargs(text=text)))

    def _only_click(self):
        self._act(ElementActionBodyCreator.click(**self._noargs()))

    def __return_attr_value(self, response):
        if "data" in response and "attrValue" in response["data"]:
            return response["data"]["attrValue"]
        else:
            return None

    def get_tag_name(self):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.get_tag_name(**self._noargs()))
        return self.__return_attr_value(response)

    def get_attr_value(self, attr):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.get_attr_value(**self._kwargs(attr=attr)))
        return self.__return_attr_value(response)

    def click(self):
        self.find_if_not_found()
        self.wait_until_clickable()
        self._only_click()

    def wait_until_clickable(self):
        self.find_if_not_found()
        self._act(ElementActionBodyCreator.wait_until_clickable(**self._noargs()))

    def wait_until_visible(self):
        self.find_if_not_found()
        self._act(ElementActionBodyCreator.wait_until_visible(**self._noargs()))

    #################################
    ### State Checking
    #################################
    def is_selected(self):
        self.find_if_not_found()
        response = self._act(ElementActionBodyCreator.is_selected(**self._noargs()))
        return response["data"]["check_passed"]

import os
import time
import base64
from setu.core.lib.setu_types import *
from setu.core.webclient.requester import SetuAgentRequester

from .automator_actions import *
from .element import GuiElement
from .multielement import GuiMultiElement
from .emd import SimpleGuiElementMetaData
from .element_container import ElementContainer
from .dropdown import GuiWebSelect
from .radio_group import GuiWebRadioGroup
from .window_handler import WindowHandler

class GuiAutomator(ElementContainer):

    def __init__(self, agent_base_url, config_dict):
        super().__init__(SetuAgentRequester(agent_base_url))
        self.agent_base_url = agent_base_url
        self.__automator_uri = "/guiauto/automator/{}".format(self.get_setu_id())
        self.config_dict = config_dict
        self.__create_screenshots_dir()
        self.__window_handler = None

    def get_window_handler(self):
        return self.__window_handler

    def get_config(self):
        return self.config_dict

    def __create_screenshots_dir(self):
        sdir = self.config_dict["SCREENSHOTS_DIR"]
        if not os.path.isdir(sdir):
            os.makedirs(sdir)

    #Override
    def _get_object_uri(self):
        return self.__automator_uri

    def launch(self):
        self._post("/launch", self.config_dict)
        self.__window_handler = WindowHandler(self)

    def go_to(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to(url=url))

    def quit(self):
        self._get("/quit")

    def take_screenshot(self):
        response = self._get("/screenshot")
        image = base64.b64decode(response["data"]["codedImage"])
        path = os.path.join(self.config_dict["SCREENSHOTS_DIR"], "{}.png".format(str(time.time()).replace(".","-")))
        f = open(path, "wb")
        f.write(image)
        f.close()

    def execute_javascript(self, js):
        self._act(TestAutomatorActionBodyCreator.execute_javascript(js))

    def switch_to_frame_by_name(self, name):
        self._act(TestAutomatorActionBodyCreator.switch_to_frame_by_name(name))

    def switch_to_frame_by_index(self, index):
        self._act(TestAutomatorActionBodyCreator.switch_to_frame_by_index(index))

    def switch_to_parent_frame(self):
        self._act(TestAutomatorActionBodyCreator.switch_to_parent_frame())

    def switch_to_root(self):
        self._act(TestAutomatorActionBodyCreator.switch_to_root())

    def switch_to_frame_of_element(self, element):
        element.find_if_not_found()
        self._act(TestAutomatorActionBodyCreator.switch_to_frame_of_element(element))

    def convert_to_select(self, gui_element):
        select = GuiWebSelect(gui_element)
        self._add_element(select.get_setu_id(), select)
        return select

    def convert_to_radiogroup(self, gui_multielement):
        rg = GuiWebRadioGroup(gui_multielement)
        self._add_element(rg.get_setu_id(), rg)
        return rg
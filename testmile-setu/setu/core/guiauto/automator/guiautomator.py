import os
import time
import base64

from setu.core.webclient.requester import SetuAgentRequester
from setu.core.guiauto.actions.automator_actions import *
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.guiauto.element.multielement import GuiMultiElement
from setu.core.guiauto.locator.emd import SimpleGuiElementMetaData
from setu.core.guiauto.base.element_container import ElementContainer
from setu.core.guiauto.element.dropdown import GuiWebSelect
from setu.core.guiauto.element.radio_group import GuiWebRadioGroup
from setu.core.config.config_types import SetuConfigOption

class GuiAutomator(ElementContainer):

    def __init__(self, agent_base_url, config):
        super().__init__(config, SetuAgentRequester(agent_base_url))
        self.__automator_uri = "/guiauto/automator/{}".format(self.get_setu_id())
        self.__create_screenshots_dir()
        self.__window_handler = None

        from .frame_handler import FrameHandler
        self.__frame_handler = FrameHandler(self)

    @property
    def window_handler(self):
        return self.__window_handler

    @property
    def frame_handler(self):
        return self.__frame_handler

    def __create_screenshots_dir(self):
        sdir = self.config.value(SetuConfigOption.SCREENSHOTS_DIR)
        if not os.path.isdir(sdir):
            os.makedirs(sdir)

    #Override
    def _get_object_uri(self):
        return self.__automator_uri

    def launch(self):
        self._post("/launch", self.config.as_json_dict())

        from .window_handler import WindowHandler
        self.__window_handler = WindowHandler(self)

    def go_to(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to(url=url))

    def quit(self):
        self._get("/quit")

    def take_screenshot(self):
        response = self._get("/screenshot")
        image = base64.b64decode(response["data"]["codedImage"])
        path = os.path.join(self.config.value(SetuConfigOption.SCREENSHOTS_DIR), "{}.png".format(str(time.time()).replace(".","-")))
        f = open(path, "wb")
        f.write(image)
        f.close()

    def execute_javascript(self, js):
        self._act(TestAutomatorActionBodyCreator.execute_javascript(js))

    def convert_to_select(self, gui_element):
        select = GuiWebSelect(gui_element)
        self._add_element(select.get_setu_id(), select)
        return select

    def convert_to_radiogroup(self, gui_multielement):
        rg = GuiWebRadioGroup(gui_multielement)
        self._add_element(rg.get_setu_id(), rg)
        return rg
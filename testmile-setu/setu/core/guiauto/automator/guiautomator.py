import base64
import os
import time

from setu.core.constants import SetuConfigOption
from setu.core.guiauto.actions.automator_actions import *
from setu.core.guiauto.base.element_container import ElementContainer
from setu.core.guiauto.element.guielement import GuiElement
from setu.core.guiauto.element.multielement import GuiMultiElement
from setu.core.guiauto.locator.emd import SimpleGuiElementMetaData
from setu.core.webclient.requester import SetuAgentRequester


class GuiAutomator(ElementContainer):

    def __init__(self, agent_base_url, config):
        super().__init__(config, SetuAgentRequester(agent_base_url))
        self.__automator_uri = "/guiauto/automator/{}".format(self.get_setu_id())
        self.__create_screenshots_dir()
        self.__window_handler = None
        self.__frame_context = "root"

        from .alert_handler import AlertHandler
        from .automator_conditions import GuiAutomatorConditions
        from .viewcontext_handler import ViewContextHandler
        from .browser_handler import BrowserHandler
        self.__alert_handler = AlertHandler(self)
        self.__conditions_handler = GuiAutomatorConditions(self)
        self.__view_handler = ViewContextHandler(self)
        self.__browser_handler = BrowserHandler(self)

    @property
    def browser(self):
        return self.__browser_handler

    @property
    def window_handler(self):
        return self.__window_handler

    @property
    def alert_handler(self):
        return self.__alert_handler

    @property
    def view_handler(self):
        return self.__view_handler

    @property
    def conditions(self):
        return self.__conditions_handler

    def get_frame_context(self):
        return self.__frame_context

    def __create_screenshots_dir(self):
        sdir = self.config.setu_config.value(SetuConfigOption.SCREENSHOTS_DIR)
        if not os.path.isdir(sdir):
            os.makedirs(sdir)

    #Override
    def _get_object_uri(self):
        return self.__automator_uri

    def launch(self):
        self._post("/launch", self.config.as_json_dict())

        from .window_handler import WindowHandler
        self.__window_handler = WindowHandler(self)

    def quit(self):
        self._get("/quit")

    def __screenshot(self):
        switch_view_context = None
        if self.config.value(SetuConfigOption.TESTRUN_TARGET_PLATFORM).lower() == "android": 
            view_name = self.view_handler.get_current_view_context()   
            if self.view_handler._does_name_represent_web_view(view_name) :
                self.view_handler.switch_to_native_view() 
                switch_view_context = view_name

        response = self._get("/screenshot")

        if switch_view_context:
            self.view_handler.switch_to_view_context(switch_view_context)
        
        return response

    def take_screenshot(self):
        response = self.__screenshot()
        image = base64.b64decode(response["data"]["codedImage"])
        path = os.path.join(self.config.value(SetuConfigOption.SCREENSHOTS_DIR), "{}.png".format(str(time.time()).replace(".","-")))
        f = open(path, "wb")
        f.write(image)
        f.close()

    def execute_javascript(self, js):
        self._act(TestAutomatorActionBodyCreator.execute_javascript(js))

    def __set_frame_context_str(self, name):
        self.__frame_context = name
        print("Automator is in {} frame".format(self.__frame_context))

    def set_frame_context(self, frame):
        self.__set_frame_context_str(frame.get_setu_id())

    def set_frame_context_as_root(self):
        self.__set_frame_context_str("root")

    def create_frame_with_locator(self, locator_name, locator_value):
        from setu.core.guiauto.element.frame import IFrame
        frame = IFrame(self, locator_name, locator_value)
        self._add_element(frame.get_setu_id(), frame)
        return frame

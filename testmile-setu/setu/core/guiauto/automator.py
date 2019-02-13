from setu.core.lib.setu_types import *
from setu.core.webclient.requester import SetuAgentRequester

from .automator_actions import *
from .element import GuiElement
from .multielement import GuiMultiElement
from .emd import SimpleGuiElementMetaData
from .element_container import ElementContainer
from .dropdown import GuiWebSelect

class GuiAutomator(ElementContainer):

    def __init__(self, agent_base_url, config_dict):
        super().__init__(SetuAgentRequester(agent_base_url))
        self.agent_base_url = agent_base_url
        self.__automator_uri = "/guiauto/automator/{}".format(self.get_setu_id())
        self.config_dict = config_dict

    #Override
    def _get_object_uri(self):
        return self.__automator_uri

    def launch(self):
        self._post("/launch", self.config_dict)

    def go_to(self, url):
        self._act(TestAutomatorActionBodyCreator.go_to(url=url))

    def quit(self):
        self._get("/quit")

    def convert_to_select(self, gui_element):
        select = GuiWebSelect(gui_element)
        self._add_element(select.get_setu_id(), select)
        return select

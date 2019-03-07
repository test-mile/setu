from setu.dispatcher.setu_actor_requester import SetuActorRequester
from setu.dispatcher.guiauto.remote.guiautomator import GuiAutomator 
from setu.dispatcher.guiauto.remote.guielement import GuiElement 

class TestSessionDispatcher:

    def __init__(self):
        self.__java_actor_url = "http://localhost:9898/setuactor"

    def guiAutomatorRemoteDispatcher(self, setu_id):
        return GuiAutomator(setu_id, SetuActorRequester(self.__java_actor_url))

    def guiElementRemoteDispatcher(self, automator_setu_id, element_setu_id):
        return GuiElement(automator_setu_id, element_setu_id, SetuActorRequester(self.__java_actor_url))

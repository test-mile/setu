from setu.core.guiauto.base.conditions import DynamicCaller, CommandCondition

class GuiElementContainerConditions:

    def __init__(self, container):
        self.__container = container

    # element could be GuiElement or MultiGuiElement
    def PresenceOf(self, element):
        caller = DynamicCaller(self.__container._find, element)
        return CommandCondition(caller)   
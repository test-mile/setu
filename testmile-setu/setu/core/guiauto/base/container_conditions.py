from setu.core.guiauto.base.conditions import DynamicCaller, CommandCondition

class GuiElementContainerConditions:

    def __init__(self, container):
        self.__container = container

    def PresenceOfElement(self, element):
        caller = DynamicCaller(self.__container._find, FinderActions.find_element, element)
        return CommandCondition(caller)   

    def PresenceOfMultiElement(self, element):
        caller = DynamicCaller(self.__container._find, FinderActions.find_multielement, element)
        return CommandCondition(caller)  
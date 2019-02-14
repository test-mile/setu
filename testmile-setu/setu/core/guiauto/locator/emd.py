
class GuiElementMetaData:

    def __init__(self, locator_dict):
        self.locator_dict = locator_dict

    def get_locators(self): # needs platform info. Then returns platform-specfic + common loctors.
        return (self.locator_dict["common"],)

class SimpleGuiElementMetaData(GuiElementMetaData):

    def __init__(self, locator_type, locator_value):
        super().__init__({"common" : (locator_type, locator_value)})

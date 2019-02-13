from .generic_element import GuiGenericElement
from .element_actions import ElementActionBodyCreator

class GuiElement(GuiGenericElement):
    
    def __init__(self, automator, emd):
        super().__init__(automator, emd, "/guiauto/element/{}")

    def _only_clear_text(self):
        self._act(ElementActionBodyCreator.clearText(**self._noargs()))

    def _only_enter_text(self, text):
        self._only_send_text(text)

    #################################
    ### Textbox abstraction
    #################################

    def clear_text(self):
        self.find_if_not_found()
        self.wait_until_clickable()
        self._only_click()
        self._only_clear_text()

    def enter_text(self, text):
        self.find_if_not_found()
        self.wait_until_clickable()
        self._only_click()
        self._only_enter_text(text)

    def set_text(self, text):
        self.find_if_not_found()
        self.wait_until_clickable()
        self._only_click()
        self._only_clear_text()
        self._only_enter_text(text)

    def has_entered_text(self, text):
        pass

    def has_entered_partial_text(self, text):
        pass

    #################################
    ### Checkbox abstraction
    #################################
    def check(self):
        self._find_if_not_found()
        self.wait_until_visible()
        if self.is_selected() is not True:
            self.wait_until_clickable()
            self._only_click()

    def uncheck(self):
        self._find_if_not_found()
        self.wait_until_visible()
        if self.is_selected() is True:
            self.wait_until_clickable()
            self._only_click()

    def toggle_checkbox(self):
        self.click()

    def is_checked(self):
        return self.is_selected()

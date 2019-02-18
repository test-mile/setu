

# Separates the underlying structure and names
# Also builds json response data where applicable
class ElementHandler:

    @classmethod
    def set_text(cls, element, text):
        element.set_text(text)

    @classmethod
    def click(cls, element):
        element.click()

    @classmethod
    def check(cls, element):
        element.check()

    @classmethod
    def uncheck(cls, element):
        element.uncheck()

    @classmethod
    def wait_until_clickable(cls, element):
        element.wait_until_clickable()

class MultiElementHandler:
    pass

class DropdownHandler:

    @classmethod
    def has_visible_text_selected(cls, dropdown, text):
        return {"checkResult" : dropdown.has_visible_text_selected(text)}

    @classmethod
    def has_value_selected(cls, dropdown, value):
        return {"checkResult" : dropdown.has_value_selected(value)}

    @classmethod
    def has_index_selected(cls, dropdown, index):
        return {"checkResult" : dropdown.has_index_selected(index)}

    @classmethod
    def get_first_selected_option_text(cls, dropdown):
        return {"checkResult" : dropdown.get_first_selected_option_text()}

    @classmethod
    def select_by_visible_text(cls, dropdown, text):
        return {"checkResult" : dropdown.select_by_visible_text(text)}

    @classmethod
    def select_by_value(cls, dropdown, value):
        return {"checkResult" : dropdown.select_by_value(value)}

    @classmethod
    def select_by_index(cls, dropdown, index):
        return {"checkResult" : dropdown.select_by_index(index)}

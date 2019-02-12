

class TestAutomatorActionBodyCreator:

    @classmethod
    def goTo(cls, **kwargs):
        return {
            "action" : "GO_TO_URL",
            "args" : kwargs
        }

    @classmethod
    def find(cls, **kwargs):
        return {
            "action" : "FIND_ELEMENT",
            "args" : kwargs
        }

class ElementActionBodyCreator:

    @classmethod
    def click(cls, **kwargs):
        return {
            "action" : "CLICK",
            "args" : kwargs
        }

    @classmethod
    def clearText(cls, **kwargs):
        return {
            "action" : "CLEAR_TEXT",
            "args" : kwargs
        }

    @classmethod
    def enterText(cls, **kwargs):
        return {
            "action" : "ENTER_TEXT",
            "args" : kwargs
        }

    @classmethod
    def wait_until_clickable(cls, **kwargs):
        return {
            "action" : "WAIT_UNTIL_CLICKABLE",
            "args" : kwargs
        }
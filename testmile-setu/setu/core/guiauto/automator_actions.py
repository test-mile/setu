

class TestAutomatorActionBodyCreator:

    @classmethod
    def go_to(cls, **kwargs):
        return {
            "action" : "GO_TO_URL",
            "args" : kwargs
        }


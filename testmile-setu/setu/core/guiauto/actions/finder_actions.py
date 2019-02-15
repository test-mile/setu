

class FinderActions:

    @classmethod
    def find_element(cls, **kwargs):
        return {
            "action" : "FIND_ELEMENT",
            "args" : kwargs
        }

    @classmethod
    def find_multielement(cls, **kwargs):
        return {
            "action" : "FIND_MULTIELEMENT",
            "args" : kwargs
        }

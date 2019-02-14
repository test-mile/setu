

class FinderActions:

    @classmethod
    def find_first_element(cls, **kwargs):
        return {
            "action" : "FIND_ELEMENT",
            "args" : kwargs
        }

    @classmethod
    def find_multi_element(cls, **kwargs):
        return {
            "action" : "FIND_MULTIELEMENT",
            "args" : kwargs
        }

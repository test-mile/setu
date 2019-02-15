

class FinderActions:

    @classmethod
    def retain_first_element(cls, **kwargs):
        return {
            "action" : "RETAIN_FIRST_ELEMENT",
            "args" : kwargs
        }

    @classmethod
    def find_multi_element(cls, **kwargs):
        return {
            "action" : "FIND_MULTIELEMENT",
            "args" : kwargs
        }

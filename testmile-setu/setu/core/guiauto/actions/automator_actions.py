

class TestAutomatorActionBodyCreator:

    @classmethod
    def _create_json_dict(cls, action, **kwargs):
        return {
            "action" : action,
            "args" : kwargs
        }

    @classmethod
    def go_to(cls, **kwargs):
        return cls._create_json_dict("GO_TO_URL", **kwargs)

    @classmethod
    def switch_to_frame(cls, **kwargs):
        return cls._create_json_dict("SWITCH_TO_FRAME", **kwargs)

    @classmethod
    def switch_to_frame_by_name(cls, name):
        return cls.switch_to_frame(byType="NAME", byValue=name)

    @classmethod
    def switch_to_frame_by_index(cls, index):
        return cls.switch_to_frame(byType="INDEX", byValue=index)

    @classmethod
    def switch_to_parent_frame(cls):
        return cls.switch_to_frame(byType="PARENT")

    @classmethod
    def switch_to_root(cls):
        return cls.switch_to_frame(byType="ROOT")

    @classmethod
    def switch_to_frame_of_element(cls, element):
        return cls.switch_to_frame(byType="ELEMENT_SETU_ID",byValue=element.get_setu_id())

    @classmethod
    def get_current_window_handle(cls):
        return cls._create_json_dict("GET_CURRENT_WINDOW_HANDLE")

    @classmethod
    def maximize_window(cls):
        return cls._create_json_dict("MAXIMIZE_WINDOW")

    @classmethod
    def get_current_window_size(cls):
        return cls._create_json_dict("GET_CURRENT_WINDOW_SIZE")

    @classmethod
    def set_window_size(cls, width, height):
        return cls._create_json_dict("SET_WINDOW_SIZE", width=width, height=height)

    @classmethod
    def get_all_window_handles(cls):
        return cls._create_json_dict("GET_ALL_WINDOW_HANDLES")

    @classmethod
    def switch_to_window(cls, handle):
        return cls._create_json_dict("SWITCH_TO_WINDOW", handle=handle)

    @classmethod
    def close_current_window(cls):
        return cls._create_json_dict("CLOSE_CURRENT_WINDOW")

    @classmethod
    def get_window_title(cls):
        return cls._create_json_dict("GET_WINDOW_TITLE")

    @classmethod
    def execute_javascript(cls, script):
        return cls._create_json_dict("EXECUTE_JAVASCRIPT", script=script)
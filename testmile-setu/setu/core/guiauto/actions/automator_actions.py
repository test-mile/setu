

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
    def jump_to_parent_frame(cls):
        return cls._create_json_dict("JUMP_TO_PARENT_FRAME")

    @classmethod
    def jump_to_html_root(cls):
        return cls._create_json_dict("JUMP_TO_HTML_ROOT")

    @classmethod
    def jump_to_frame(cls, element, **kwargs):
        return cls._create_json_dict("JUMP_TO_FRAME", byType="ELEMENT_SETU_ID",byValue=element.get_setu_id(), **kwargs)

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

    @classmethod
    def is_alert_present(cls):
        return cls._create_json_dict("IS_ALERT_PRESENT")

    @classmethod
    def confirm_alert(cls):
        return cls._create_json_dict("CONFIRM_ALERT")

    @classmethod
    def dismiss_alert(cls):
        return cls._create_json_dict("DISMISS_ALERT")

    @classmethod
    def send_text_to_alert(cls, text):
        return cls._create_json_dict("SEND_TEXT_TO_ALERT",text=text)

    @classmethod
    def get_text_from_alert(cls):
        return cls._create_json_dict("GET_TEXT_FROM_ALERT")

    @classmethod
    def switch_to_view_context(cls, view_name):
        return cls._create_json_dict("SWITCH_TO_VIEW_CONTEXT",viewContext=view_name)

    @classmethod
    def get_current_view_context(cls):
        return cls._create_json_dict("GET_CURRENT_VIEW_CONTEXT")

    @classmethod
    def get_all_view_contexts(cls):
        return cls._create_json_dict("GET_ALL_VIEW_CONTEXTS")
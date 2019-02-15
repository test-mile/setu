
class ElementActionBodyCreator:

    @classmethod
    def _create_json_dict(cls, action, **kwargs):
        return {
            "action" : action,
            "args" : kwargs
        }

    @classmethod
    def click(cls, **kwargs):
        return cls._create_json_dict("CLICK", **kwargs)

    @classmethod
    def clearText(cls, **kwargs):
        return cls._create_json_dict("CLEAR_TEXT", **kwargs)

    @classmethod
    def send_text(cls, **kwargs):
        return cls._create_json_dict("SEND_TEXT", **kwargs)

    @classmethod
    def is_selected(cls, **kwargs):
        return cls._create_json_dict("IS_SELECTED", **kwargs)

    @classmethod
    def is_visible(cls, **kwargs):
        return cls._create_json_dict("IS_VISIBLE", **kwargs)

    @classmethod
    def is_clickable(cls, **kwargs):
        return cls._create_json_dict("IS_CLICKABLE", **kwargs)

    @classmethod
    def get_tag_name(cls, **kwargs):
        return cls._create_json_dict("GET_TAG_NAME", **kwargs)

    @classmethod
    def get_attr_value(cls, **kwargs):
        return cls._create_json_dict("GET_ATTR_VALUE", **kwargs)

    @classmethod
    def get_text_content(cls, **kwargs):
        return cls._create_json_dict("GET_TEXT_CONTENT", **kwargs)
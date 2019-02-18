

class SetuSvcObjectManager:
    GUIAUOTMATOR_HANDLERS = {}

    @classmethod
    def register_gui_automator_handler(cls, handler):
        cls.GUIAUOTMATOR_HANDLERS[handler.setu_id] = handler

    @classmethod
    def deregister_gui_automator_handler(cls, handler):
        del cls.GUIAUOTMATOR_HANDLERS[handler.setu_id]

    @classmethod
    def get_gui_automator_handler(cls, setu_id):
        return cls.GUIAUOTMATOR_HANDLERS[setu_id]
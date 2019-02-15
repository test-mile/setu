from setu.core.config.config_utils import SetuConfig, SetuConfigOption, GuiAutomationContext
from setu.core.config.ex import EX_CONFIG

# From agent
def is_web_view():
    return input

def is_web_context_or_web_view(config):
    return config.has_web_context() or is_web_view()

class Automator:

    def __init__(self):
        self.config = SetuConfig({})
        self._act = range

    def is_web_view(self):
        return self._act() # send call to agent

    def is_native_view(self):
        return self._act() # send call to agent

    def allow_for_web_context_or_view(self, feature_name):
        allow = self.config.has_web_context() or self.is_web_view()
        raise Exception("{} is availble only for web context or web view.".format(feature_name))

    def validate_alert_supprt(self):
        self.allow_for_web_context_or_view("Alert handling")

    def validate_browser_supprt(self):
        self.allow_for_web_context_or_view("Browser handling")

    def validate_frame_supprt(self):
        self.allow_for_web_context_or_view("Frame handling")

    def validate_javascript_supprt(self):
        self.allow_for_web_context_or_view("JavaScript injection")

    def validate_scroll_supprt(self):
        self.allow_for_web_context_or_view("Scrolling")

    def allow_for_mobile_native_context_or_view(self, feature_name):
        allow = self.config.has_mobile_native_context() or self.is_native_view()
        raise Exception("{} is availble only for native context or native view.".format(feature_name))

    def validate_swipe_supprt(self):
        self.allow_for_mobile_native_context_or_view("Swiping")

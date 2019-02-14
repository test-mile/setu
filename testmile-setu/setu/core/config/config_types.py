from enum import Enum, auto

class SetuConfigOption(Enum):
    ROOT_DIR = auto()
    LOG_DIR = auto()
    SCREENSHOTS_DIR = auto()
    
    TESTRUN_ENVIRONMENT = auto()
    TESTRUN_TARGET_PLATFORM = auto()
    TESTRUN_TARGET_PLATFORM_VERSION = auto()

    GUI_AUTOMATOR_NAME = auto()
    
    BROWSER_NAME = auto()
    BROWSER_VERSION = auto()
    BROWSER_MAXIMIZE = auto()
    BROWSER_DIM_HEIGHT = auto()
    BROWSER_DIM_WIDTH = auto()
    BROWSER_BIN_PATH = auto()
    BROWSER_PROXY_ON = auto()
    
    GUIAUTO_CONTEXT = auto()
    GUIAUTO_SCROLL_PIXELS = auto()
    GUIAUTO_SWIPE_TOP = auto()
    GUIAUTO_SWIPE_BOTTOM = auto()
    GUIAUTO_SWIPE_MAX_WAIT = auto()
    GUIAUTO_MAX_WAIT = auto()
    
    MOBILE_DEVICE_NAME = auto()
    MOBILE_DEVICE_UDID = auto()
    MOBILE_APP_FILE_PATH = auto()
    
    SELENIUM_DRIVER_PROP = auto()
    SELENIUM_DRIVERS_DIR = auto()
    SELENIUM_DRIVER_PATH = auto()
    
    APPIUM_HUB_URL = auto()
    APPIUM_AUTO_LAUNCH = auto()
    
    IMAGE_COMPARISON_MIN_SCORE = auto()
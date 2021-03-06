from setu.core.constants import SetuConfigOption
from setu.dispatcher.broker import SetuActorDriverConfigOption
import copy
import pprint

class DriverCapabilities:
    # Selenium
    UNEXPECTED_ALERT_BEHAVIOUR = "unexpectedAlertBehaviour" # accept,dismiss,ignore
    UNHANDLED_PROMPT_BEHAVIOUR = "unhandledPromptBehavior" # accept,dismiss,ignore
    ELEMENT_SCROLL_BEHAVIOR = "elementScrollBehavior" #???
    AUTOMATION_NAME = "automationName"
    BROWSER_NAME = "browserName"
    BROWSER_VERSION = "browserVersion"

    # Appium
    PLATFORM_NAME = "platformName"
    PLATFORM_VERSION = "platformVersion"
    DEVICE_NAME = "deviceName"
    APP_PATH = "app"
    DEVICE_UDID = "udid"
    NEW_COMMAND_TIMEOUT = "newCommandTimeout" # unit: seconds
    AUTO_WEBVIEW = "autoWebview" # Default false
    NO_RESET = "noReset" # Default false
    FULL_RESET = "fullReset"
    CLEAR_SYSTEM_FILES = "clearSystemFiles"

    # Android
    ANDROID_APP_ACTIVITY = "appActivity"
    ANDROID_APP_PACKAGE = "appPackage"
    ANDROID_WAIT_ACTIVITY = "appWaitActivity"
    ANDROID_WAIT_PACKAGE = "appWaitPackage"
    ANDROID_UNICODE_KEYBOARD = "unicodeKeyboard"
    ANDROID_RESET_KEYBOARD = "resetKeyboard"

    #ios
    IOS_BUNDLE_ID = "bundleId"
    IOS_AUTO_ACCEPT_ALERTS = "autoAcceptAlerts"

    def __init__(self, config, json_dict):
        self.__config = config
        self.__out_dict = {
            "setuOptions" : {},
            "userOptions" : config.user_config.as_json_dict(),
            "browserArgs": [],
            "driverCapabilities": {},
            "browserPreferences":{},
            "browserExtensions":[]
        }

        pprint.pprint(config.as_json_dict())

        self.__process_config(config)
        self.__process(json_dict)

        aname = self.__config.setu_config.value(SetuConfigOption.GUIAUTO_AUTOMATOR_NAME).name.lower()
        acontext = self.__config.setu_config.value(SetuConfigOption.GUIAUTO_CONTEXT).name.lower()
        aplatform = self.__config.setu_config.value(SetuConfigOption.MOBILE_OS_NAME).name.lower()

        if aname == "selenium":
            self.__process_for_selenium(json_dict)
        elif aname == "appium":
            self.__process_for_appium(json_dict)
            if aplatform.lower() == "android":
                self.__process_for_android(json_dict)
            elif aplatform.lower() == "ios":
                self.__process_for_ios(json_dict)

            if acontext.lower() == "mobile_web":
                if aplatform.lower() == "android":
                    self.__process_for_android_web(json_dict)
                elif aplatform.lower() == "ios":
                    self.__process_for_ios_web(json_dict)
            elif acontext.lower() == "mobile_native":
                if aplatform.lower() == "android":
                    self.__process_for_android_native(json_dict)
                elif aplatform.lower() == "ios":
                    self.__process_for_ios_native(json_dict)
            elif acontext.lower() == "mobile_hybrid":
                if aplatform.lower() == "android":
                    self.__process_for_android_hybrid(json_dict)
                elif aplatform.lower() == "ios":
                    self.__process_for_ios_hybrid(json_dict)
        
        if not self.__out_dict["browserArgs"]:
            del self.__out_dict["browserArgs"]
        if not self.__out_dict["driverCapabilities"]:
            del self.__out_dict["driverCapabilities"]
        if not self.__out_dict["browserPreferences"]:
            del self.__out_dict["browserPreferences"]
        if not self.__out_dict["browserExtensions"]:
            del self.__out_dict["browserExtensions"]

    @property
    def processed_config(self):
        return self.__out_dict

    @property
    def _config(self):
        return self.__config

    def __process_config(self, config):
        self.__out_dict["automationContext"] = config.setu_config.value(SetuConfigOption.GUIAUTO_CONTEXT).name.upper()
        temp_d = config.setu_config.as_json_dict()
        for k,v in temp_d.items():
            if k in SetuActorDriverConfigOption.__members__:
                self.__out_dict["setuOptions"][k] = v
        pprint.pprint(self.__out_dict)
        

    def __process(self, dict_from_requester):
        self.__out_dict["driverCapabilities"][self.UNEXPECTED_ALERT_BEHAVIOUR] = "dismiss"
        self.__out_dict["driverCapabilities"][self.UNHANDLED_PROMPT_BEHAVIOUR] = "dismiss"

        if not dict_from_requester: return
        if "browserArgs" in dict_from_requester and dict_from_requester["browserArgs"]:
            self.__out_dict["browserArgs"].extend(dict_from_requester["browserArgs"])
        if "driverCapabilities" in dict_from_requester and dict_from_requester["driverCapabilities"]:
            self.__out_dict["driverCapabilities"].update(
                {i:j for i,j in dict_from_requester["driverCapabilities"].items() if j !="not_set"})
        if "browserPreferences" in dict_from_requester and dict_from_requester["browserPreferences"]:
            self.__out_dict["browserPreferences"] = dict_from_requester["browserPreferences"]
        if "browserExtensions" in dict_from_requester and dict_from_requester["browserExtensions"]:
            self.__out_dict["browserExtensions"].extend(dict_from_requester["browserExtensions"])

    def __process_for_selenium(self, in_dict):
        self.__out_dict["driverCapabilities"][self.BROWSER_NAME] = self._config.setu_config.value(SetuConfigOption.BROWSER_NAME).name
        if self._config.setu_config.value(SetuConfigOption.BROWSER_VERSION) != "not_set":
            self.__out_dict["driverCapabilities"][self.BROWSER_VERSION] = self._config.setu_config.value(SetuConfigOption.BROWSER_VERSION)

    def __process_for_appium(self, dict_from_requester):
        mobile_os_name = self._config.setu_config.value(SetuConfigOption.MOBILE_OS_NAME).name
        if mobile_os_name.lower() == "android":
            self.__out_dict["driverCapabilities"][self.PLATFORM_NAME] = "Android"
        elif mobile_os_name.lower() == "ios":
            self.__out_dict["driverCapabilities"][self.PLATFORM_NAME] = "iOS"
        self.__out_dict["driverCapabilities"][self.NEW_COMMAND_TIMEOUT] = 300 # 5 minutes 
        self.__out_dict["driverCapabilities"][self.PLATFORM_VERSION] = self._config.setu_config.value(SetuConfigOption.MOBILE_OS_VERSION)
        self.__out_dict["driverCapabilities"][self.DEVICE_NAME] = self._config.setu_config.value(SetuConfigOption.MOBILE_DEVICE_NAME)
        self.__out_dict["driverCapabilities"][self.APP_PATH] = self._config.setu_config.value(SetuConfigOption.MOBILE_APP_FILE_PATH)
        self.__out_dict["driverCapabilities"][self.DEVICE_UDID] = self._config.setu_config.value(SetuConfigOption.MOBILE_DEVICE_UDID)

    def __process_for_android(self, dict_from_requester):
        self.__out_dict["driverCapabilities"][self.AUTOMATION_NAME] = "UiAutomator2"
        self.__out_dict["driverCapabilities"][self.ANDROID_UNICODE_KEYBOARD] = True
        self.__out_dict["driverCapabilities"][self.ANDROID_RESET_KEYBOARD] = True

    def __process_for_android_native(self, dict_from_requester):
        self.__out_dict["driverCapabilities"][self.ANDROID_APP_ACTIVITY] = self._config.setu_config.value(SetuConfigOption.MOBILE_APP_PACKAGE).name
        self.__out_dict["driverCapabilities"][self.ANDROID_APP_PACKAGE] = self._config.setu_config.value(SetuConfigOption.MOBILE_APP_ACTIVITY)
        # self.__out_dict["capabilites"][self.ANDROID_WAIT_ACTIVITY] = self._config.setu_config.value(SetuConfigOption.MOBILE_APP_ACTIVITY)
        # self.__out_dict["capabilites"][self.ANDROID_WAIT_PACKAGE] = self._config.setu_config.value(SetuConfigOption.MOBILE_APP_FILE_PATH)

    def __process_for_android_web(self, dict_from_requester):
        # Browser
        browser_name = self._config.setu_config.value(SetuConfigOption.BROWSER_NAME).name
        if browser_name.lower() != "chrome":
            raise Exception("{} is not a valid browser for Android.".format(browser_name))
        self.__out_dict["capabilities"][self.BROWSER_NAME] = browser_name

    def __process_for_android_hybrid(self, dict_from_requester):
        pass

    def __process_for_ios(self, dict_from_requester):
        self.__out_dict["driverCapabilities"][self.AUTOMATION_NAME] = "XCUITest"
        self.__out_dict["driverCapabilities"][self.IOS_AUTO_ACCEPT_ALERTS] = True

    def __process_for_ios_native(self, dict_from_requester):
        pass

    def __process_for_ios_web(self, dict_from_requester):
                self.__out_dict["driverCapabilities"][self.BROWSER_NAME] = self._config.setu_config.value(SetuConfigOption.BROWSER_NAME).name

    def __process_for_ios_hybrid(self, dict_from_requester):
        pass



'''
	
#Common (WebDriver)
BROWSER_NAME = "browserName"
BROWSER_VERSION = "browserVersion"

#Appium
PLATFORM_NAME = "platformName"
PLATFORM_VERSION = "platformVersion"
DEVICE_NAME = "deviceName"
APP_PATH = "app"
DEVICE_UDID = "udid"

Android{
// Android Specific
ANDROID_APP_ACTIVITY = "appActivity"
ANDROID_APP_PACKAGE = "appPackage"
ANDROID_WAIT_ACTIVITY = "appWaitActivity"
ANDROID_WAIT_PACKAGE = "appWaitPackage"
}

IOS {

}
'''
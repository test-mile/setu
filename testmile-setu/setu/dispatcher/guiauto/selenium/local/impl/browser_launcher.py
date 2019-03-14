from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import *
from selenium.webdriver import Remote

class BrowserLauncher:

    @classmethod
    def launch(cls, config):
        driver_path = config["setuOptions"]["SELENIUM_DRIVER_PATH"]
        browser_bin_path = config["setuOptions"]["BROWSER_BIN_PATH"]
        browser_name = config["setuOptions"]["BROWSER_NAME"]
        return CREATOR_MAP[browser_name](config, driver_path, browser_bin_path)

    @classmethod
    def _create_chrome(cls, config, driver_path, browser_bin_path):
        from selenium.webdriver import Chrome, ChromeOptions

        caps = DesiredCapabilities.CHROME
        caps.update(config["driverCapabilities"])

        if config["setuOptions"]["BROWSER_PROXY_ON"]:
            proxy = Proxy()
            proxy_string = "{}.{}".format(
                config["setuOptions"]["BROWSER_PROXY_HOST"],
                config["setuOptions"]["BROWSER_PROXY_PORT"]
            )
            proxy.http_proxy = proxy_string
            proxy.ssl_proxy = proxy_string
            proxy.add_to_capabilities(caps)

        options = ChromeOptions()

        if browser_bin_path.lower() != "not_set":
            options.binary_location = browser_bin_path

        if "browserPreferences" in config and config["browserPreferences"]:
            options.add_experimental_option("prefs", config["browserPreferences"])

        if "browserArgs" in config and config["browserArgs"]:
            for arg in config["browserArgs"]:
                options.add_argument(arg)

        if "browserExtensions" in config and config["browserExtensions"]:
            for ext in config["browserExtensions"]:
                options.add_extension(ext)

        caps[ChromeOptions.KEY] = options.to_capabilities()[ChromeOptions.KEY]

        return Chrome(executable_path=driver_path, desired_capabilities=caps)

    @classmethod
    def _create_firefox(cls, config, driver_path, browser_bin_path):
        from selenium.webdriver import Firefox
        from selenium.webdriver import FirefoxOptions
        from selenium.webdriver import FirefoxProfile

        profile = FirefoxProfile()
        if config["setuOptions"]["BROWSER_PROXY_ON"]:
            proxy = Proxy()
            proxy_string = "{}.{}".format(
                config["setuOptions"]["BROWSER_PROXY_HOST"],
                config["setuOptions"]["BROWSER_PROXY_PORT"]
            )
            proxy.http_proxy = proxy_string
            proxy.ssl_proxy = proxy_string
            profile.set_proxy(proxy)

        caps = DesiredCapabilities.FIREFOX
        caps.update(config["driverCapabilities"])

        options = FirefoxOptions()

        if browser_bin_path.lower() != "not_set":
            options.binary_location = browser_bin_path

        if config["browserPreferences"]:
            for pref, value in config["browserPreferences"].items():
                options.set_preference(pref, value)

        if config["browserArgs"]:
            for arg in config["browserArgs"]:
                options.add_argument(arg)

        driver =  Firefox(executable_path=driver_path, firefox_profile=profile, capabilities=caps)

        if config["browserExtensions"]:
            for ext in config["browserExtensions"]:
                driver.install_addon(ext)

        return driver

    @classmethod
    def _create_safari(cls, config, driver_path, browser_bin_path):
        from selenium.webdriver import Safari

        caps = DesiredCapabilities.SAFARI
        caps.update(config["driverCapabilities"])

        return Safari(executable_path=driver_path, desired_capabilities=caps)


CREATOR_MAP = {
    "FIREFOX" : BrowserLauncher._create_firefox,
    "CHROME" : BrowserLauncher._create_chrome,
    "SAFARI" : BrowserLauncher._create_safari,
}

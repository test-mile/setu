
class DriverCommands:

    @classmethod
    def go_to_url(cls, driver, url):
        driver.get(url)

    @classmethod
    def refresh_browser(cls, driver):
        driver.refresh()

    @classmethod
    def go_back_in_browser(cls, driver):
        driver.back()

    @classmethod
    def go_forward_in_browser(cls, driver):
        driver.forward()

    @classmethod
    def quit(cls, driver):
        driver.quit()

    @classmethod
    def get_page_title(cls, driver):
        return driver.title

    @classmethod
    def get_url(cls, driver):
        return driver

    @classmethod
    def get_page_source(cls, driver):
        return driver.page_source

    @classmethod
    def is_web_alert_present(cls, driver):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            WebDriverWait(browser, 1).until(EC.alert_is_present(),'Timed out.')
            return True
        except:
            return False

    @classmethod
    def confirm_web_alert(cls, driver):
        driver.switch_to.alert.confirm()

    @classmethod
    def dismiss_web_alert(cls, driver):
        driver.switch_to.alert.dismiss()

    @classmethod
    def send_text_to_web_alert(cls, driver, text):
        driver.switch_to.alert.send_keys(text)

    @classmethod
    def get_text_from_web_alert(cls, driver):
        return driver.switch_to.alert.text

    @classmethod
    def focus_on_frame(cls, driver, element):
        driver.switch_to.frame(element)

    @classmethod
    def focus_on_dom_root(cls, driver):
        return driver.switch_to.default_content()

    @classmethod
    def focus_on_parent_frame(cls, driver):
        driver.switch_to.parent_frame()

    @classmethod
    def execute_javascript(cls, driver, script):
        return driver.execute_javascript(script)

    @classmethod
    def take_screenshot(cls, driver):
        return driver.get_screenshot_as_base64()

    @classmethod
    def set_window_size(cls, driver, width, height):
        driver.set_window_size(width, height)

    @classmethod
    def maximize_window(cls, driver):
        driver.maximize_window()

    @classmethod
    def get_current_window_handle(cls, driver):
        return driver.current_window_handle

    @classmethod
    def focus_on_window(cls, driver, windowHandle):
        driver.switch_to.window(windowHandle)

    @classmethod
    def close_current_window(cls, driver):
        driver.close()

    @classmethod
    def get_window_title(cls, driver):
        return driver.title

    @classmethod
    def get_current_window_size(cls, driver):
        return driver.get_window_size()

    @classmethod
    def get_all_winodw_handles(cls, driver):
        return driver.window_handles
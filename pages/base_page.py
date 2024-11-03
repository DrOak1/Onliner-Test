from abc import ABC, abstractmethod

from driver.web_driver import Driver


class BasePage(ABC):
    def __init__(self, driver: Driver):
        self.driver = driver

    JS_REMOVE_ELEMENT = "arguments[0].remove();"

    @abstractmethod
    def page_locator(self):
        pass

    @abstractmethod
    def cookie_banner_locator(self):
        pass

    def is_page_open(self, name=None):
        return self.driver.find_element(self.page_locator()).is_displayed()

    def scroll_to_footer(self, footer_locator):
        footer = self.driver.find_element(footer_locator)
        self.driver.scroll_to_element(footer)

    def remove_cookie_banner(self):
        banner = self.driver.find_element(self.cookie_banner_locator())
        self.driver.execute_script(self.JS_REMOVE_ELEMENT, banner)

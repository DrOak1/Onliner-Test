from driver.web_driver import Driver
from pages.base_page import BasePage


class OnlinerPageLocators:
    MAIN_NAVIGATION = "//div[contains(@class, 'navigation_overflow')]"
    PHONE_CATALOG = "//span[text()='Смартфоны']"


class OnlinerPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    def page_locator(self):
        return OnlinerPageLocators.MAIN_NAVIGATION

    def cookie_banner_locator(self):
        pass

    def go_to_mobile_phone_catalog(self):
        self.driver.click(OnlinerPageLocators.PHONE_CATALOG)

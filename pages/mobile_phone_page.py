from driver.web_driver import Driver
from pages.base_page import BasePage
from utils.string_operations import StringOperations


class MobilePhonePageLocators:
    PAGE_HEADER = "//h1[contains(@class, 'catalog-masthead')]"
    PHONE_DESCRIPTION = "//div[contains(@class, 'offers-description__specs')]/p"


class MobilePhonePage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    def is_page_open(self, name=None):
        if name is not None:
            phone_name = self.driver.find_element(MobilePhonePageLocators.PAGE_HEADER).text
            return phone_name == name
        else:
            return super().is_page_open()

    def page_locator(self):
        return MobilePhonePageLocators.PAGE_HEADER

    def cookie_banner_locator(self):
        pass

    def get_phone_param_from_page(self):
        phone_description = self.driver.find_element(MobilePhonePageLocators.PHONE_DESCRIPTION).text
        param = StringOperations.extract_device_specs(phone_description)
        return param

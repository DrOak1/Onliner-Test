from driver.web_driver import Driver
from pages.base_page import BasePage
from pages.enums.compare_page_enum import ComparePageEnum


class ComparePageLocators:
    COMPARE_PAGE_HEADER = "//h1[text()='Сравнение товаров']"
    COMPARE_TABLE = "(//span[text() = '{param}']/ancestor::tr//span[contains(@class, 'text')])"


class ComparePage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    def page_locator(self):
        return ComparePageLocators.COMPARE_PAGE_HEADER

    def cookie_banner_locator(self):
        pass

    def get_compare_param(self, phone_number, *args):
        params = []
        for arg in args:
            element = self.driver.find_element(
                ComparePageLocators.COMPARE_TABLE.format(param=arg) + f"[{phone_number}]").text.replace('"', '')
            if arg == ComparePageEnum.RAM:
                element = f"ОЗУ {element}"
            if arg == ComparePageEnum.MEMORY:
                element = f"память {element}"
            params.append(element)
        return params

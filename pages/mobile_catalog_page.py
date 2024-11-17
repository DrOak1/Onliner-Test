from driver.web_driver import Driver
from pages.base_page import BasePage
from pages.forms.filters import Filters
from utils.string_operations import StringOperations


class MobileCatalogPageLocators:
    CATALOG_TITLE = "//h1[contains(@class,'title')]"
    COMPARE_LINK = "//a[contains(@class, 'catalog-interaction')]"
    FOOTER = "//footer"
    COOKIE_BANNER = "//div[contains(@class, 'auth-popup_width_full')]"
    PHONE = "(//a[contains(@class, 'semibold')])"
    PHONE_CATALOG = "//div[contains(@class, 'offers-part')]//div[contains(@class, 'part_1')]"
    PHONE_PRICE = "//div[not(contains(@class, 'special'))]/a[contains(@href, 'prices')]/span[not(@class)]"
    PHONE_OS = "/descendant::div[contains(@class, 'description_small')][1]"
    PHONE_SCREEN_SIZE = "/descendant::div[contains(@class, 'description_small')][2]"
    PHONE_RAM = "/descendant::div[contains(@class, 'description_small')][4]"
    PHONE_MEMORY = "/descendant::div[contains(@class, 'description_small')][5]"


class MobileCatalogPage(BasePage):

    def __init__(self, driver: Driver):
        super().__init__(driver)
        self.filters = Filters(self.driver)

    def page_locator(self):
        return MobileCatalogPageLocators.CATALOG_TITLE

    def cookie_banner_locator(self):
        return MobileCatalogPageLocators.COOKIE_BANNER

    def add_to_compare_two_phone(self, first, second):
        self.scroll_to_footer(MobileCatalogPageLocators.FOOTER)
        self.filters.add_to_compare(first)
        self.filters.add_to_compare(second)

    def get_phones_name(self, phone):
        return self.driver.find_element(MobileCatalogPageLocators.PHONE + f"[{phone}]").text

    def update_phones_index(self, phone_names):
        header = self.driver.find_element(MobileCatalogPageLocators.CATALOG_TITLE)
        self.driver.scroll_to_element(header)
        phones = self.driver.find_elements(MobileCatalogPageLocators.PHONE)
        indices = []

        for index, phone in enumerate(phones, start=1):
            if phone.text == phone_names[0] or phone.text == phone_names[1]:
                indices.append(index)

        return indices[0], indices[1]

    def get_price(self, index):
        price_element = self.driver.find_element(
            f"({MobileCatalogPageLocators.PHONE_PRICE})[{index}]"
        )
        return StringOperations.convert_str_number_to_float(price_element.text)

    def get_screen_size(self, index):
        size_element = self.driver.find_element(
            f"({MobileCatalogPageLocators.PHONE_CATALOG})[{index}]{MobileCatalogPageLocators.PHONE_SCREEN_SIZE}"
        )
        screen_size, _ = StringOperations.extract_screen_size_and_dimension(size_element.text)
        return screen_size.replace('.', '')

    def go_to_phone_page(self, phone_number):
        phone = self.driver.find_element(MobileCatalogPageLocators.PHONE + f"[{phone_number}]")
        self.driver.click_by_js(phone)

    def go_to_compare_page(self):
        compare_link = self.driver.find_element(MobileCatalogPageLocators.COMPARE_LINK)
        compare_link.click()

    def is_phone_displayed(self, phone_number):
        return self.driver.find_element(MobileCatalogPageLocators.PHONE + f"[{phone_number}]").is_displayed()

    def get_phone_param(self, phone_number):
        os = self.driver.find_element(
            f"({MobileCatalogPageLocators.PHONE_CATALOG})[{phone_number}]{MobileCatalogPageLocators.PHONE_OS}").text
        screen = (self.driver.find_element(
            f"({MobileCatalogPageLocators.PHONE_CATALOG})[{phone_number}]{MobileCatalogPageLocators.PHONE_SCREEN_SIZE}")
                  .text)
        ram = self.driver.find_element(
            f"({MobileCatalogPageLocators.PHONE_CATALOG})[{phone_number}]{MobileCatalogPageLocators.PHONE_RAM}").text
        memory = self.driver.find_element(
            f"({MobileCatalogPageLocators.PHONE_CATALOG})[{phone_number}]{MobileCatalogPageLocators.PHONE_MEMORY}").text

        screen_size = StringOperations.extract_screen_size_and_dimension(screen)[0]
        screen_dimension = StringOperations.extract_screen_size_and_dimension(screen)[1]

        param = [os, screen_size, screen_dimension, ram, memory]
        return param

    def is_compare_link_exists(self):
        return self.driver.find_element(MobileCatalogPageLocators.COMPARE_LINK).is_displayed()

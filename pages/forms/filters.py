from selenium.webdriver.support.select import Select
from driver.web_driver import Driver
from pages.enums.compare_page_enum import ComparePageEnum
from pages.enums.filter_enum import FilterEnum
from utils.string_operations import StringOperations


class FiltersLocators:
    ADD_TO_COMPARE_CHECKBOX = "//div[contains(@class, 'warning')]/input"
    CHECKBOX_LABEL = "(//div[contains(@class, 'warning')]/input/ancestor::label)[{index}]"
    FILTER_HOLDER = "(//div[contains(@class, 'tag-list')])/descendant::div[contains(text(),'{value}')]"
    FROM_PRICE = "//input[@placeholder = 'от']"
    TO_PRICE = "//input[@placeholder = 'до']"
    FROM_SCREEN_SIZE = "(//div[text()='{value}']/ancestor::div[contains(@class, 'condensed-other')]//select)[1]"
    TO_SCREEN_SIZE = "(//div[text()='{value}']/ancestor::div[contains(@class, 'condensed-other')]//select)[2]"


class Filters:
    def __init__(self, driver: Driver):
        self.driver = driver

    def add_to_compare(self, phone_number):
        checkbox_list = self.driver.find_elements(FiltersLocators.ADD_TO_COMPARE_CHECKBOX)
        self.driver.click_by_js(checkbox_list[phone_number - 1])

    def checkbox_status(self, phone_number):
        return self.driver.find_element(
            FiltersLocators.CHECKBOX_LABEL.format(index=phone_number)).get_attribute("title")

    def is_checkbox_set(self, first_checkbox):
        return self.checkbox_status(first_checkbox) == FilterEnum.IN_COMPARISON

    def is_checkbox_displayed(self, checkbox_index):
        return self.driver.find_element(FiltersLocators.CHECKBOX_LABEL.format(index=checkbox_index)).is_displayed()

    def set_price_filter(self, from_price=None, to_price=None):
        if from_price:
            self.driver.find_element(FiltersLocators.FROM_PRICE).send_keys(from_price)
            self.check_filter_set('{:.0f}'.format(from_price))
        if to_price:
            self.driver.find_element(FiltersLocators.TO_PRICE).send_keys(to_price)

    def check_filter_set(self, filter_value):
        filter_status_locator = FiltersLocators.FILTER_HOLDER.format(value=filter_value)
        return self.driver.find_element_presence(filter_status_locator).is_displayed()

    def set_screen_size(self, from_size=None, to_size=None):
        if from_size:
            from_selector = self.driver.find_element_presence(
                FiltersLocators.FROM_SCREEN_SIZE.format(value=ComparePageEnum.SCREEN_SIZE)
            )
            self.driver.scroll_to_element(from_selector)
            self.load_selector_options(from_selector)
            from_screen_size = Select(from_selector)
            from_screen_size.select_by_value(from_size)
            self.check_filter_set(StringOperations.add_decimal_point(from_size))
        if to_size:
            to_selector = self.driver.find_element_presence(
                FiltersLocators.TO_SCREEN_SIZE.format(value=ComparePageEnum.SCREEN_SIZE)
            )
            self.driver.scroll_to_element(to_selector)
            self.load_selector_options(to_selector)
            to_screen_size = Select(to_selector)
            to_screen_size.select_by_value(to_size)

    def load_selector_options(self, selector):
        self.driver.move_to_element(selector)
        selector.click()

import random
import pytest
from config.config_loader import load_config
from driver.web_driver import Driver
from pages.compare_page import ComparePage
from pages.enums.compare_page_enum import ComparePageEnum
from pages.mobile_catalog_page import MobileCatalogPage
from pages.mobile_phone_page import MobilePhonePage
from pages.onliner_page import OnlinerPage
from utils.random_utils import RandomUtils
from utils.string_operations import StringOperations


@pytest.fixture(scope="session")
def config():
    return load_config('../config/config.json')


@pytest.fixture(scope="session")
def browser():
    driver = Driver()
    yield driver
    driver.close_driver()


def test_onliner(browser, config):
    random_value = RandomUtils.get_random_value()
    browser.go_to_site(config['onliner_url'])
    onliner_page = OnlinerPage(browser)
    assert onliner_page.is_page_open(), "Main page is not opened"

    onliner_page.go_to_mobile_phone_catalog()
    mobile_catalog_page = MobileCatalogPage(browser)
    assert mobile_catalog_page.is_page_open(), "Mobile phones catalog is not opened"

    mobile_catalog_page.remove_cookie_banner()
    mobile_catalog_page.add_to_compare_two_phone(random_value[0], random_value[1])
    names = mobile_catalog_page.get_phones_name(random_value[0]), mobile_catalog_page.get_phones_name(random_value[1])
    assert mobile_catalog_page.is_compare_link_exists(), "Compare link doesn't exist"
    assert (mobile_catalog_page.filters.is_checkbox_set(random_value[0]) &
            mobile_catalog_page.filters.is_checkbox_set(random_value[1])), "Checkbox is not set"

    prices = mobile_catalog_page.get_price(random_value[0]), mobile_catalog_page.get_price(random_value[1])
    mobile_catalog_page.filters.set_price_filter(min(prices), max(prices))
    assert (mobile_catalog_page.filters.check_filter_set('{:.0f}'.format(prices[0])) &
            mobile_catalog_page.filters.check_filter_set('{:.0f}'.format(prices[1]))), "Price filter is not set"

    new_phones_number = mobile_catalog_page.update_phones_index(names)
    screen_sizes = mobile_catalog_page.get_screen_size(new_phones_number[0]), mobile_catalog_page.get_screen_size(
        new_phones_number[1])
    mobile_catalog_page.filters.set_screen_size(min(screen_sizes), max(screen_sizes))
    assert (mobile_catalog_page.filters.check_filter_set(
        StringOperations.add_decimal_point(screen_sizes[0])) &
            mobile_catalog_page.filters.check_filter_set(StringOperations.add_decimal_point(screen_sizes[1]))), \
        "Screen size filter is not set"

    new_phones_number = mobile_catalog_page.update_phones_index(names)
    assert (mobile_catalog_page.is_phone_displayed(new_phones_number[0]) &
            mobile_catalog_page.is_phone_displayed(new_phones_number[1])), "Phone is not displayed"
    assert (mobile_catalog_page.filters.is_checkbox_displayed(new_phones_number[0]) &
            mobile_catalog_page.filters.is_checkbox_displayed(new_phones_number[1])), "Checkbox is not displayed"

    rand_phone = random.choice(new_phones_number)
    param = mobile_catalog_page.get_phone_param(rand_phone)
    phone_name = mobile_catalog_page.get_phones_name(rand_phone)
    mobile_catalog_page.go_to_phone_page(rand_phone)
    phone_page = MobilePhonePage(browser)
    assert phone_page.is_page_open(phone_name), "Phone page doesn't opened"
    param_from_phone_page = phone_page.get_phone_param_from_page()
    assert param == param_from_phone_page, "Phone params are not equal"

    browser.go_back()
    assert mobile_catalog_page.is_page_open(), "Catalog page is not opened"
    first_phone_param = mobile_catalog_page.get_phone_param(new_phones_number[0])
    second_phone_param = mobile_catalog_page.get_phone_param(new_phones_number[1])
    mobile_catalog_page.go_to_compare_page()
    compare_page = ComparePage(browser)
    assert compare_page.is_page_open(), "Compare page is not opened"
    first_compare_param = compare_page.get_compare_param(1, ComparePageEnum.OS,
                                                         ComparePageEnum.SCREEN_SIZE, ComparePageEnum.SCREEN_DIMENSION,
                                                         ComparePageEnum.RAM, ComparePageEnum.MEMORY)
    second_compare_param = compare_page.get_compare_param(2, ComparePageEnum.OS,
                                                          ComparePageEnum.SCREEN_SIZE, ComparePageEnum.SCREEN_DIMENSION,
                                                          ComparePageEnum.RAM, ComparePageEnum.MEMORY)
    assert (first_phone_param == first_compare_param) & (second_phone_param == second_compare_param), \
        "Phones params are not equal"

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config.config_loader import load_config
from driver.waits import Waits


class Driver:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.waits = Waits(self.driver, load_config('../config/config.json')["waiting_time"])

    JS_SCROLL = ("window.scrollTo(0, arguments[0].getBoundingClientRect().top "
                     "+ window.pageYOffset - window.innerHeight / 2);")
    JS_CLICK = "arguments[0].click();"

    def go_to_site(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.waits.wait_element_visible((By.XPATH, locator))

    def find_elements(self, locator):
        return self.waits.wait_for_all_element_presence((By.XPATH, locator))

    def find_element_presence(self, locator):
        return self.waits.wait_element_presence((By.XPATH, locator))

    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def scroll_to_element(self, element):
        self.execute_script(self.JS_SCROLL, element)

    def click(self, locator):
        element = self.waits.wait_element_clickable((By.XPATH, locator))
        element.click()

    def click_by_js(self, web_element):
        self.execute_script(self.JS_CLICK, web_element)

    def go_back(self):
        self.driver.back()

    def move_to_element(self, element):
        ActionChains(self.driver) \
            .scroll_to_element(element) \
            .perform()

    def close_driver(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()

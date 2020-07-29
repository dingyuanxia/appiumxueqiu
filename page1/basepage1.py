from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from UI自动化框架2.page1.wrapper import handle_black


class BasePage:
    _driver: WebDriver
    _black_list = [(By.ID, "iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def finds(self, locator, value):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

        # try:
        #     return self._driver.find_element(locator, value)
        # except:
        #     for black in self._black_list:
        #         elements = self._driver.find_elements(*black)
        #         if len(elements) > 0:
        #             elements[0].click()
        #         break
        #         #查找到黑名单后再次找原来的元素
        #     return self.find(locator, value)

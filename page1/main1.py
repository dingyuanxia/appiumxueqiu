from selenium.webdriver.common.by import By

from UI自动化框架2.page1.basepage1 import BasePage
from UI自动化框架2.page1.market1 import Market


class Main(BasePage):
    def goto_market(self):
        self.find(By.XPATH, "//*[@text='行情']").click()
        return Market(self._driver)

from selenium.webdriver.common.by import By

from UI自动化框架2.page1.basepage1 import BasePage
from UI自动化框架2.page1.search1 import Search


class Market(BasePage):
    def goto_search(self):
        #self.find(By.ID, "com.xueqiu.android:id/action_search").click()
        return Search(self._driver)
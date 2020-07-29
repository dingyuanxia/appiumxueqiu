from selenium.webdriver.common.by import By

from UI自动化框架2.page1.basepage1 import BasePage


class Search(BasePage):
    def search(self, name):
        self.find(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.find(By.XPATH, f"//*[@text='{name}']").click()
        #点击加自选
        self.find(By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/ll_stock_item_container']//*[@text='{name}']/../..//*[@text='加自选']").click()

    def is_choose(self, name):
        eles = self.finds(By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/ll_stock_item_container']//*[@text='{name}']/../..//*[@text='已添加']")
        return len(eles) > 0
from appium import webdriver

from UI自动化框架2.page1.basepage1 import BasePage
from UI自动化框架2.page1.main1 import Main


class App(BasePage):
        _appPackage = 'com.xueqiu.android'
        _appActivity = '.view.WelcomeActivityAlias'

        def start(self):
            if self._driver is None:

                des_caps = {
                    "platformName": 'Android',
                    'platformVersion': '7.0',
                    'deviceName': "0123456789ABCDEF",
                    'noReset': "true",
                    'appPackage': self._appPackage,
                    'appActivity': self._appActivity
                }
                self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
            else:
                self._driver.start_activity(self._appPackage, self._appActivity)
            self._driver.implicitly_wait(10)
            return self

        def main(self) -> Main:
            return Main(self._driver)
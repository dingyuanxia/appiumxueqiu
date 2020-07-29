from selenium.webdriver.common.by import By




def handle_black(func):
    def wrapper(*args, **kwargs):
        from UI自动化框架2.page1.basepage1 import BasePage
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _error_num = 0
        instance:BasePage=args[0]
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            instance._driver.implicitly_wait(10)
            return element

        except Exception as e:
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1

            for black in _black_list:
                eles = instance.finds(*black)
                if len(eles) > 0:
                    eles[0].click()
                return wrapper(*args, **kwargs)
            raise e

    return wrapper

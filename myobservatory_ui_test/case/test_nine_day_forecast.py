import re
import allure
from appium.webdriver.common.mobileby import MobileBy
from lib.forecast_driver import Driver
from lib.elements import ElementsId,ElementsAccessibilityId
from lib.util import date_format_today, date_format_tomorrow, date_format_nine_day
import time


class TestCase():

    def setup_method(self):
        self.driver = Driver()
        self.driver.open_more_option()
        self.driver.swipe2_nine_day()

    def teardown_method(self):
        self.driver.close_app()
        self.driver.quit()

    @allure.title('进入九天预报页面后判断首屏信息是否正确')
    def test_nine_day_forecast_001(self):
        assert self.driver.find_element_wait(MobileBy.ACCESSIBILITY_ID, ElementsAccessibilityId.tab_list_nine_day_forecast).text == '九天预报'
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.tab_list_local_forecast).text  == '本港预报'
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.tab_extension_clause_forecast).text == '延伸条款'
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.tab_extension_clause_forecast).text == '天气预报'

    @allure.title('进入九天预报页面后判断首屏返回最近两天的天气预报信息是否正确')
    def test_nine_day_forecast_002(self):
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.datetime_today).text == date_format_today()
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.datetime_tomorrow).text == date_format_tomorrow()

    @allure.title('校验九天预报页面的聊天机器人是否展示')
    def test_nine_day_forecast_003(self):
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.chatbot).text  == '聊天机械人'

    @allure.title('tab页面切换后返回至九天预报页面展示正常')
    def test_nine_day_forecast_004(self):
        assert self.driver.find_element_wait(MobileBy.ACCESSIBILITY_ID, ElementsAccessibilityId.tab_list_nine_day_forecast).text == '九天预报'
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.tab_list_local_forecast).text  == '本港预报'
        self.driver.click_local_forecast()
        time.sleep(2)
        self.driver.tab_click_nine_day_forecast()
        assert self.driver.find_element_wait(MobileBy.ACCESSIBILITY_ID,
                                             ElementsAccessibilityId.tab_list_nine_day_forecast).text == '九天预报'
        assert self.driver.find_element_by_accessibility_id(
            ElementsAccessibilityId.tab_list_local_forecast).text == '本港预报'


    @allure.title('滑动至最底部展示9天的天气预报情况')
    def test_nine_day_forecast_005(self):
        assert self.driver.find_element_wait(MobileBy.ACCESSIBILITY_ID,
                                             ElementsAccessibilityId.tab_list_nine_day_forecast).text == '九天预报'
        assert self.driver.find_element_by_accessibility_id(
            ElementsAccessibilityId.tab_list_local_forecast).text == '本港预报'
        self.driver.swipe2end()
        time.sleep(2)
        assert self.driver.find_element_by_accessibility_id(ElementsAccessibilityId.datetime_today).text == date_format_nine_day()

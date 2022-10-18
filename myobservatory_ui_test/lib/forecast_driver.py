from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conf import env as config
from lib.elements import ElementsId,ElementsAccessibilityId
import time


class Driver(WebDriver):

    def __init__(self):
        super().__init__(f'http://{config.ip}:{config.port}/wd/hub',config.forecast)
        self.implicitly_wait(60)
        self.wait = WebDriverWait(self, 60, 0.5)

    def is_element_exist(self,by,element):
        flag = True
        try:
            self.find_element(by,element)
            return flag
        except:
            flag = False
            return flag

    def swipe2_nine_day(self):
        '''
        下滑至九天预报的位置
        :return:
        '''
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("九天预报").instance(0));').click()

    def open_more_option(self):
        '''
        进入左上角更多选项页面
        :return:
        '''
        self.find_element_by_accessibility_id(ElementsAccessibilityId.more_btn).click()

    def click_nine_day_forecast(self):
        '''
        首页点击进入九天预报
        :return:
        '''
        self.find_element_by_id(ElementsId.nine_day_forecast).click()
        self.find_element_by_accessibility_id(ElementsAccessibilityId.btn_list_nine_day_forecast).click()

    def tab_click_nine_day_forecast(self):
        '''
        tab页点击进入九天预报
        :return:
        '''
        self.find_element_by_id(ElementsId.nine_day_forecast).click()
        self.find_element_by_accessibility_id(ElementsAccessibilityId.btn_list_nine_day_forecast).click()

    def click_local_forecast(self):
        '''
        点击进入本港预报
        :return:
        '''
        self.find_element_by_accessibility_id(ElementsAccessibilityId.tab_list_local_forecast).click()

    def click_ext_forecast(self):
        '''
        点击延伸预报
        :return:
        '''
        self.find_element_by_accessibility_id(ElementsAccessibilityId.tab_extension_clause_forecast).click()

    def swipe2end(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0):
        # 获取屏幕大小
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        # 屏幕从下向上滑动(方向：滑到底部）
        # 宽度x:居中不变，均为width*0.5
        # 高度y:从最高位置height*0.9到最低位置height*0.1
        # duration:1000  滑动保证稳定性
        self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, 1000)
        for i in range(4):
            self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, 1000)



if __name__ == '__main__':
    d=Driver()

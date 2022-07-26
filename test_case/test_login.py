import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from business.action import huadong
from business.setting.denglu import login

from business.setting.into_setting import shezhi
from config.mht_capabilities import getDriver
from data.getData import getdata
import warnings

class TestCase(unittest.TestCase):
    dataFile="../data/denglu.csv"
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.mhtDriver=getDriver(False)
        huadong(self.mhtDriver)
        shezhi(self.mhtDriver)
    def testNormal(self):
        #第一个测试用例，正常登陆
        data=getdata(self.dataFile,1)
        login(self.mhtDriver,data[0],data[1],data[2])
        # denglu(self.mhtDriver,data[0],data[1],data[2])
        sleep(2)
        find=self.mhtDriver.find_element_by_android_uiautomator('new UiSelector().text("登入成功")')
        self.assertIsNotNone(find)
    def testErrorName(self):
        data = getdata(self.dataFile, 2)
        login(self.mhtDriver, data[0], data[1], data[2])
        self.wait=WebDriverWait(self.mhtDriver,5,0.02)
        result=self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[contains(@text,"错误")]'))).text
        print(result)
    def tearDown(self):
        pass
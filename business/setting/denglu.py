from time import sleep

from business.action import huadong
from business.setting.into_setting import shezhi
from config.mht_capabilities import getDriver
from data.getData import getdata


def login(appDriver,ip,username,passwd):
    #点击店内登录
    appDriver.find_element_by_id("com.emicro.emicrophone:id/textView1").click()
    sleep(2)
    #点击输入ip地址
    appDriver.find_element_by_id("com.emicro.emicrophone:id/userlogin_serverip").send_keys(ip)
    sleep(2)
    #点击输入用户名
    appDriver.find_element_by_id("com.emicro.emicrophone:id/userlogin_username").send_keys(username)
    #密码
    sleep(2)
    appDriver.find_element_by_id("com.emicro.emicrophone:id/userlogin_passwrod").send_keys(passwd)
    #点击登录按钮
    sleep(2)
    appDriver.find_elements_by_class_name("android.widget.TextView")[5].click()

if __name__ == '__main__':
    driver = getDriver(False)
    huadong(driver)
    shezhi(driver)
    data=getdata("../../data/denglu.csv",4)
    denglu(driver,data[0],data[1],data[2])
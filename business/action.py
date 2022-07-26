from time import sleep

from config.mht_capabilities import getDriver


def huadong(appDriver):
    #获取手机屏幕高和宽
    width=appDriver.get_window_size()["width"]
    height=appDriver.get_window_size()['height']
    print(width)
    print(height)

    x_start=0.9*width
    x_end=0.1*width
    y_start=0.5*height
    y_end=0.5*height

    for i in range(0,2):
        appDriver.swipe(x_start,y_start,x_end,y_end)
        sleep(2)

    appDriver.find_element_by_id("com.emicro.emicrophone:id/bottom_start").click()

if __name__ == '__main__':
    driver=getDriver(False)
    huadong(driver)
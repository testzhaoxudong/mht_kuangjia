import os
from time import sleep

import yaml
from appium import webdriver


def getDriver(isInstall):
    base_dir=os.path.dirname(__file__)
    yaml_path=os.path.join(base_dir,"capabilities.yaml")
    with open(yaml_path,'r',encoding='utf-8') as mht_file:
        desire_cap=yaml.load(mht_file,Loader=yaml.FullLoader)
        print(desire_cap)

    if isInstall:
        pro_dir=os.path.dirname(base_dir)
        desire_cap['app']=os.path.join(pro_dir,'app',desire_cap['appName'])
    # print(desire_cap)
    url="http://"+desire_cap["appiumIp"]+':'+str(desire_cap["appiumPort"])+'/wd/hub'
    appDriver=webdriver.Remote(url,desire_cap)
    sleep(3)
    return appDriver

if __name__ == '__main__':
    getDriver(True)
#如果手机上没有安装app
#当参数是False，表示已经安装
#当参数是True，表示需要安装
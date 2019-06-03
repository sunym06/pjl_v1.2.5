from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class why():
    driver= WebDriver

    @classmethod
    def come(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "FFK0217330000388"
        caps["appPackage"] = "com.great_mall.u4"
        caps["appActivity"] = "io.dcloud.PandoraEntryActivity"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        # caps['noReset']=True
        # caps['chromedriverExecutableDir']="/Users/seveniruby/projects/chromedriver/2.20"
        # caps['unicodeKeyboard']=True
        # caps['resetKeyboard']=True
        nae = "ttt"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

a = why()
# a.com.('//*[@text="我的"]').click()
a.come().find_element_by_xpath('//*[@text="我的"]').click()
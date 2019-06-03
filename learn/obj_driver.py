from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class Android():
    driver= WebDriver
    @classmethod
    def installApp(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        # caps['noReset']=True
        # caps['chromedriverExecutableDir']="/Users/seveniruby/projects/chromedriver/2.20"
        # caps['unicodeKeyboard']=True
        # caps['resetKeyboard']=True
        nae = "ttt"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

a = Android()
a.installApp().find_element_by_xpath("//*[@text='基金']").click()
# a.driver.find_element_by_xpath("//contains(@id,'基金')").click()
# a.driver.find_element_by_xpath("//*[@text='基金']").click()

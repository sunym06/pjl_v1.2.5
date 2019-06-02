from driver.AndroidClient import AndroidClient

class BasePage(object):
    def __init__(self):
        print('init')
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        print('getDriver')

        cls.driver=AndroidClient.driver
        print('getd')
        return cls.driver

a = BasePage.getDriver()

#
# a = AndroidClient
# print(type(a))
# print(type(a.driver))
# # a.driver.find_element_by_xpath('//*[@text="我的"]').click()
#
#
# # tit_my = a.driver.find_element_by_xpath('//*[@text="我的"]').click()
# # log = driver.find_element_by_xpath('//*[@text="登录/注册"]').click()
# # ph = driver.find_element_by_id('phone').send_keys('15801287634')
# # ph = driver.find_element_by_id('password').send_keys('aaa12345')
# # driver.find_element_by_id('login').click()
#
# # driver.find_element_by_xpath('//*[@text="我的"]').click()
# # driver.find_element_by_xpath('//*[@text="正在拍"]').click()
# # driver.find_element_by_id('personal_data').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('//*[@text="我拍中"]').click()
# # driver.find_element_by_id('personal_data').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('//*[@text="未拍中"]').click()
# # driver.find_element_by_id('personal_data').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('//*[@text="已关注"]').click()
# # driver.find_element_by_id('personal_data').click()
# # time.sleep(2)
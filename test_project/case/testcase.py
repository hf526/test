#coding=utf-8
import requests,unittest,json,time
from public.browser import browser
from public.public import BasePage
from data.PMS import Pms



class Imcloud_Flow(unittest.TestCase):
    def setUp(self):
        driver = browser()
        driver=driver.open_browser()
        self.pms = Pms(driver)
    def tearDown(self):
        pass
    def test_login(self):
        self.pms.sleep(1)
        self.pms.rebutton()
    def test_login2(self):
        self.pms.sleep(1)
        self.pms.input_username()
        self.pms.sleep(1)
        self.pms.input_password()
        self.pms.sleep(1)
        self.pms.loginbutton()
        self.pms.sleep(5)




if __name__ == '__main__':
    unittest.main()
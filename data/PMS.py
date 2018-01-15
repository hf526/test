from public.public import BasePage
from selenium import webdriver

username='css=>form > div:nth-child(1) input'
name='cw5212'
password='css=>form > div:nth-child(2) input'
pd='123456789'
login_button='css=>button'
re_button='css=>.el-message-box__btns .el-button--primary'
class Pms(BasePage):
        def input_username(self):
            self.type(username,name)
        def input_password(self):
            self.type(password,pd)
        def rebutton(self):
            self.click(re_button)
        def loginbutton(self):
            self.click(login_button)

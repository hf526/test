#coding=utf-8
import requests,unittest,json,time,os,ConfigParser
from log import Logger
from selenium import webdriver

logger = Logger().get_loger()
class BasePage(object):
    def __init__(self, driver):
        self.driver =driver
    def quit(self):
        self.driver.quit()
        logger.info("quit browser")
    def back(self):
        self.driver.back()
        logger.info("back browser")
    def forward(self):
        self.driver.forward()
        logger.info("go browser")
    def max(self):
        driver.maximize_window()
        # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)
        # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing the browser.")
        except NameError as e:
            logger.error("Failed to close the browser with %s" % e)
            # 保存图片
    def screen(self):
        file_path = s.path.dirname(os.getcwd())+"/pictures/"
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.screen()
    def find(self, selector):
        element=''
        try :
            if '=>' in selector:
                by = selector.split('=>')[0]
                value = selector.split('=>')[1]
                if by == "id":
                    element = self.driver.find_element_by_id(value)
                elif by == "name":
                    element = self.driver.find_element_by_name(value)
                elif by == "tagName":
                    element = self.driver.find_element_by_tagName(value)  # 元素的标签名称来查找元素
                elif by == "className":
                    element = self.driver.find_element_by_className(value)
                elif by == "linktext":
                    element = self.driver.find_element_by_linkText(value)  # 超文本链接上的文字信息来定位元素
                elif by == "text":
                    element = self.driver.find_element_by_partialLinkText(value)  # 超链接上的文本信息或者只想通过一些关键字进行匹配
                elif by == "xpath":
                    element = self.driver.find_element_by_xpath(value)
                elif by == "css":
                    element = self.driver.find_element_by_css_selector(value)
                else:
                    logger.error(" data error")
                return element
            else:
                logger.error(" data error")
        except:
            logger.error(" =>  does not exist" )
    def type(self, selector, text):
        el = self.find(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()
    def click(self, selector):
        el = self.find(selector)
        try:
            el.click()
            logger.info("The element was clicked." )
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
    def window(self):
        return self.driver.current_window_handle  # 获取当前窗口
        logger.info("get browser window")
    def windows(self):
        return self.driver.window_handles  # 获取全部窗口
        logger.info("get browser windows")
    def cwindow(self, c):
        return self.driver.switch_to_window(c)  # 选择窗口
        logger.info("switch the browser windows")
    def get_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title
        logger.info("get browser title" )
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
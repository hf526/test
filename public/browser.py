#codng=utf-8
import os,ConfigParser
from log import Logger
from selenium import webdriver


class browser():
    logger = Logger().get_loger()
    def open_browser(self):
        config = ConfigParser.ConfigParser()
        path = os.getcwd()
        path = 'F:\hf/config/config.ini'  # os.path.dirname(path)+
        print path
        config.read(path)
        Type = config.get("browserType", "Name")
        URL= config.get("testServer", "URL")
        if Type == 'Chrome':
            self.driver = webdriver.Chrome()
            self.driver.get(URL)
            self.logger.info('open the Chrome browser')
        elif Type == 'Firefox':
            self.driver = webdriver.Firefox()
            self.driver.get(URL)
            self.logger.info('open the Firefox browser')
        elif Type == 'IE':
            self.driver = webdriver.IE()
            self.driver.get(URL)
            self.logger.info('open the IE browser')
        else:
            self.logger.info('this config read error')
        return self.driver


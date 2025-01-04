import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utilities.customLogger import LogGen
import time
from utilities.readProperties import ReadConfig

from pageObjects.LoginPage import Login

class Test_001_login:

    baseUrl = ReadConfig.getApplicationURL()
    # print(baseUrl)
    search_text = ReadConfig.getsearchtext()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.log()

    def test_homePageTitle(self, setup):
        self.logger.info("*************************************")
        self.logger.info("**************** test the home page title *********************")
        self.driver = setup
        # print(self.baseUrl)
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*****************test is passed**********")
        else:
            assert False
            self.logger.error("************testcase_failed****************************")

    # def test_search_text(self, setup):
    #      self.logger.info("*****************************************")
    #      self.logger.info("***************testcase search text started***********************")
    #      self.driver = setup
    #      self.driver.get(self.baseUrl)
    #      time.sleep(5)
    #      self.obj = Login(self.driver)
    #      self.obj.set_search_name(self.search_text)
    #      self.obj.click_search()
    #      act_title = self.driver.title
    #      # print(f"{self.search_text} - Wikipedia")
    #      if act_title == f"{self.search_text} - Wikipedia":
    #          self.driver.close()
    #          self.logger.info("******************text case passed*******************")
    #          assert True
    #      else:
    #          self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
    #          self.logger.error("********************test case is failed*****************")
    #          assert False

    def test_login(self,setup):
        self.driver = setup
        self.obj = Login(self.driver)
        self.driver.get(self.baseUrl)

        time.sleep(1)
        self.obj.setUserName(self.username)
        time.sleep(1)
        self.obj.setPassword(self.password)
        time.sleep(1)
        self.obj.clickLogin()
        time.sleep(7)
        title = self.driver.title
        if title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False




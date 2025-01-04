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
from utilities import XLUtils

from pageObjects.LoginPage import Login

class Test_002_login:  #this is the program in which we are giving excel file and we are getting the data input and expected result
                        #then we are checking the condition and matching everything from it
    baseUrl = ReadConfig.getApplicationURL()
    # print(baseUrl)
    path = ".//TestData/text_search.xlsx"
    logger = LogGen.log()

    def test_search_text_ddt(self, setup):
         self.logger.info("*****************************************")
         self.logger.info("***************testcase search text started***********************")
         self.driver = setup
         self.driver.get(self.baseUrl)
         time.sleep(5)
         self.rows = XLUtils.getRow(self.path, "Sheet1")
         list_results = []
         print(f"{self.rows} are max rows in sheet")
         for i in range(2,self.rows+1):  #it will generate the values from 0 to row-1, so that why we use row+1
             print(XLUtils.readData(self.path,"Sheet1", i,1))
             search_text = XLUtils.readData(self.path,"Sheet1", i,1)
             expected_result = XLUtils.readData(self.path,"Sheet1", i,2)
             self.obj = Login(self.driver)
             self.obj.set_search_name(search_text)
             self.obj.click_search()
             title = self.driver.title
             if title == "Saurabh Pandey - Wikipedia":
                 if expected_result == "Pass" :
                     self.logger.info("********PASS*****")
                     list_results.append("Pass")
                 elif expected_result == "Fail":
                     self.logger.info("*****FAIL*****")
                     list_results.append("Fail")
             elif title != "Saurabh Pandey - Wikipedia":
                 if expected_result == "Fail" :
                     self.logger.info("********PASS*****")
                     list_results.append("Pass")
                 elif expected_result == "Pass":
                     self.logger.info("*****FAIL*****")
                     list_results.append("Fail")
             self.driver.back()
         print(list_results)
         if "Fail" not in list_results:
              self.driver.close()
              assert True
         else:
             self.driver.close()
             assert False






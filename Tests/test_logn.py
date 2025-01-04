import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException

from Config.config import Test_config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("init_driver")
class Testlogin:

    def test_home(self):
        print(f"the title of the website is {self.driver.title}")
        assert self.driver.title == "OrangeHRM"


    def test_loginPage(self):
        self.driver.get(Test_config.URL)
        time.sleep(4)
        username = self.driver.find_element(By.XPATH,"//input[@name='username']")
        password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        username.send_keys("Admin")
        password.send_keys("admin123")
        time.sleep(4)
        btn = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        btn.click()
        time.sleep(3)
        assert self.driver.find_element(By.TAG_NAME,"h6").text == "Dashboard"

    def test_addUser(self):
        self.driver.get(Test_config.URL)
        self.driver.maximize_window()
        #Implicit wait
        self.driver.implicitly_wait(10)
        time.sleep(4)
        admin = self.driver.find_element(By.CSS_SELECTOR,"a[href='/web/index.php/admin/viewAdminModule']")
        admin.click()
        time.sleep(4)
        button = self.driver.find_element(By.CLASS_NAME,"oxd-icon.bi-plus")
        button.click()
        time.sleep(4)
        role = self.driver.find_elements(By.CLASS_NAME,"oxd-select-text-input")
        role[0].click()
        time.sleep(4)
        sub_role = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@role='listbox']//child::div[2]")))
        sub_role.click()
        # Ranga Akunuri
        Emp_name = self.driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']")
        fluent = WebDriverWait(self.driver,10,poll_frequency = 5, ignored_exceptions=[NoSuchElementException])
        Emp_name.click()
        Emp_name.send_keys("Ranga Akunuri")
        role[1].click()
        # status = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@role='listbox']//child::div[2]")))
        status = fluent.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']//child::div[2]")))
        status.click()
        username = self.driver.find_element(By.CLASS_NAME,"oxd-input.oxd-input--active")
        username.send_keys("bcd")
        password = self.driver.find_element(By.XPATH,"//input[@type='password']")
        time.sleep(4)
        # name_clk =
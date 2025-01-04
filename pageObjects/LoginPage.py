from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[contains(text(),'Log in')]"
    button_search_xpath = "//i[contains(text(),'Search')]"
    link_logout_linktext="Logout"  #text having the link
    textbox_search = "searchInput"
    name = "search"
    input_xpath = "//input[@id='searchInput']"

    def __init__(self,driver): #constructor which will be invoker at the time of object creation
        self.driver=driver        #and the driver is coming from the test case which is the assigned to our local variable and we will use it for our purposes

    def set_search_name(self, text):
        self.driver.find_element(By.ID, self.textbox_search).clear()
        self.driver.find_element(By.ID, self.textbox_search).send_keys(text)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
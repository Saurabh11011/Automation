from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver as uc
import pytest

BROWSER_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application/brave.exe"
OPTIONS = Options()
OPTIONS.binary_location = BROWSER_PATH
# options = Options()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(options=OPTIONS)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(options=OPTIONS)
    return driver

def pytest_addoption(parser):       #this will get the value frm CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):           #This will return the browser value to setup method
    return request.config.getoption("--browser")

########################pytest html report#####################################

#It is hook for adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Wikipedia'
#     config._metadata['Module Name'] = 'Text Search'
#     config._metadata['Tester'] = 'Saurabh'
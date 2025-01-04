import pytest
from selenium import webdriver
from Config.config import Test_config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def init_driver(request):
    option = Options()
    option.binary_location = Test_config.BROWSER_PATH
    driver = webdriver.Chrome(options=option)
    driver.get(Test_config.URL)
    request.cls.driver = driver
    yield
    driver.quit()



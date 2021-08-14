import pytest
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from utils.services import Services

@pytest.fixture(scope="function")
def driver_setup(request):
     from selenium import webdriver
     options = ChromeOptions()
     driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
     driver.get('https://wordpress.com/me')
     driver.maximize_window()

     yield
     driver.quit()

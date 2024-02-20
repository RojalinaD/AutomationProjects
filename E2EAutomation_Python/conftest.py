import pytest
from selenium import webdriver
import pytest_html

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\AllDrivers\chromedriver_win32\chromedriver.exe")


    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\AllDrivers\geckodriver-v0.29.1-win64\geckodriver.exe")


    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\AllDrivers\edgedriver_win64\msedgedriver.exe")


    driver.get("https://www.godaddy.com/")
    driver.maximize_window()
    driver.implicitly_wait(6)
    request.cls.driver = driver
    #yield
    #driver.close()


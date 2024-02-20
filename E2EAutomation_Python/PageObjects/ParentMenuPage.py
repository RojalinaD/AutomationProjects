#//div[@class='parent-menu-panel']//ul/li[1]
from selenium.webdriver.common.by import By


class ParentMenuPage:

    parentmenulinks = (By.XPATH, "//li[@class='menu fmenu']")
    parentdomainname = (By.XPATH, "//li[@data-track-name='Domain_Names']")

    def __init__(self, driver):
        self.driver = driver

    def getParentMenuLinks(self):
        return self.driver.find_elements(*ParentMenuPage.parentmenulinks)

    def getParentDomainName(self):
        return self.driver.find_element(*ParentMenuPage.parentdomainname)
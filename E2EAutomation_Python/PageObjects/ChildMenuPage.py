from selenium.webdriver.common.by import By


class ChildMenuPage:


    childdomainname =(By.XPATH, "//a[@data-track-name='Domain_Names']")
    childmenulinks = (By.XPATH, "//div[@id='subnav-domain_names']//div[1]//ul//li")

    def __init__(self, driver):
        self.driver = driver

    def getChildDomainName(self):
        return self.driver.find_element(*ChildMenuPage.childdomainname)

    def getChildMenuLinks(self):
        return self.driver.find_elements(*ChildMenuPage.childmenulinks)

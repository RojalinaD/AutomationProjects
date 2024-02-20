from selenium.webdriver.common.by import By


class SearchDomainPage:

    #search_domain = (By.XPATH, "//input[@name='domainToCheck']")

    search_domain = (By.XPATH, "//input[@aria-label='Find your perfect domain']")
    search_btn = (By.CSS_SELECTOR, "button[aria-label='Search']")

    def __init__(self,driver):
        self.driver = driver

    def getSearchDomain(self):
        return self.driver.find_element(*SearchDomainPage.search_domain)

    def getSearchButton(self):
        return self.driver.find_element(*SearchDomainPage.search_btn)


from selenium.webdriver.common.by import By

class HomePage:
    login_drpdown = (By.XPATH, "//details[@data-track-name='account_dropdown']//span[3]")
    signinbtn = (By.XPATH, "//div[@class='sign-in']/ul/li/a")
    menu_btn = (By.XPATH, "//button[@class='product-flyout-btn']")
    cart_btn = (By.XPATH, "//a[@aria-label='Cart']")
    domain_search = (By.XPATH, "//input[@name='domainToCheck']")
    search_btn = (By.XPATH, "//button[@aria-label='Search Domain']")
    review_txt = (By.XPATH, "//div[@class='testimonial-text']")

    def __init__(self, driver):
        self.driver = driver

    def getLoginBtn(self):
        return self.driver.find_element(*HomePage.login_drpdown)

    def getSignInBtn(self):
        return self.driver.find_element(*HomePage.signinbtn)

    def getMenuBtn(self):
        return self.driver.find_element(*HomePage.menu_btn)

    def getCartBtn(self):
        return self.driver.find_element(*HomePage.cart_btn)

    def getDomainSearchField(self):
        return self.driver.find_element(*HomePage.domain_search)

    def getSearchButton(self):
        return self.driver.find_element(*HomePage.search_btn)

    def getReviewsTxt(self):
        return self.driver.find_elements(*HomePage.review_txt)

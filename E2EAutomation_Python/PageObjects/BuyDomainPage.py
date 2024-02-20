from selenium.webdriver.common.by import By


class BuyDomainPage:

    get_domain_btn = (By.XPATH, "//span[normalize-space()='Get It']")
    text_successmsg = (By.XPATH, "//div[@class='ms0 mb-0']")
    btn_gotocart = (By.XPATH, "//span[normalize-space()='Continue to Cart']")


    def __init__(self,driver):
        self.driver = driver

    def getSuccessTxt(self):
        return self.driver.find_element(*BuyDomainPage.text_successmsg)

    def getDomainBtn(self):
        return self.driver.find_element(*BuyDomainPage.get_domain_btn)

    def getGoToCart(self):
        return self.driver.find_element(*BuyDomainPage.btn_gotocart)


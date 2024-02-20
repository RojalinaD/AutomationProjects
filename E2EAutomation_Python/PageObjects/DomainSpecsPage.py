from selenium.webdriver.common.by import By


class DomainSpecsPage:

    #btn_gotocart = (By.XPATH, "//button[@id='stickyContinue']/span")
    #btn_gotocart = (By.LINK_TEXT, "Continue to Cart")
    btn_gotocart = (By.XPATH, "//button[@id='stickyContinue' or type='button']")
    #btn_gotocart = (By.XPATH, "//button[@id='stickyContinue']//span[@class='ux-button-text'][normalize-space()='Continue to Cart']")


    def __init__(self, driver):
        self.driver = driver

    def getGoToCartBtn(self):
        return self.driver.find_element(*DomainSpecsPage.btn_gotocart)
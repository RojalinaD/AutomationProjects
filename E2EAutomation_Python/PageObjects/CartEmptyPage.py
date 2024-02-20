from selenium.webdriver.common.by import By


class CartEmptyPage:

    msg_emptycart = (By.XPATH, "//span[@class='text-muted text-center py-2']")
    msg_shopping = (By.CSS_SELECTOR, "span[class='font-weight-bold']")


    def __init__(self, driver):
        self.driver = driver

    def getMsgEmptyCart(self):
        return self.driver.find_element(*CartEmptyPage.msg_emptycart)

    def getMsgShopping(self):
        return self.driver.find_element(*CartEmptyPage.msg_shopping)



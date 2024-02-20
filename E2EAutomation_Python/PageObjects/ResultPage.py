from selenium.webdriver.common.by import By


class ResultPage:

    #result_text = (By.XPATH, "//div[@class='ms0 mb-0']")
    result_text1 = (By.CSS_SELECTOR, ".ms0.mb-0")
    result_text2 = (By.CSS_SELECTOR, ".d-inline.ml-1")

    def __init__(self,driver):
        self.driver = driver

    def getResultText1(self):
        return self.driver.find_element(*ResultPage.result_text1)

    def getResultText2(self):
        return self.driver.find_element(*ResultPage.result_text2)




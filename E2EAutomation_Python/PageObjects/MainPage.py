from selenium.webdriver.common.by import By


class MainPage:

    profilename = (By.XPATH, "//div[@class='customer-name']")
    popupwindow = (By.XPATH, "//div[@id='Yourbrowserisabitunusual-modal-dialog']//div")
    okaybtn = (By.XPATH, "//div[@id='Yourbrowserisabitunusual-modal-dialog']//div//div[3]//button")

    def __init__(self, driver):
        self.driver = driver

    def getProfileName(self):
        return self.driver.find_element(*MainPage.profilename)

    def getPopupWindow(self):
        return self.driver.find_element(*MainPage.popupwindow)

    def getOkayButton(self):
        return self.driver.find_element(*MainPage.okaybtn)


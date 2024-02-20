from selenium.webdriver.common.by import By

class SignInPage:

    uname = (By.ID, "username")
    pwd = (By.ID, "password")
    chkbox = (By.ID, "remember-me")
    submitbtn = (By.ID, "submitBtn")

    def __init__(self, driver):
        self.driver = driver

    def getunamefield(self):
        return self.driver.find_element(*SignInPage.uname)

    def getpwdfield(self):
        return self.driver.find_element(*SignInPage.pwd)

    def getcheckbox(self):
        return self.driver.find_element(*SignInPage.chkbox)

    def getSubmitBtn(self):
        return self.driver.find_element(*SignInPage.submitbtn)

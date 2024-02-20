import time



from PageObjects.HomePage import HomePage
from PageObjects.MainPage import MainPage
from PageObjects.SignInPage import SignInPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_signIn(self):

        homepage = HomePage(self.driver)
        homepage.getLoginBtn().click()
        homepage.getSignInBtn().click()
        time.sleep(6)

        signinpage = SignInPage(self.driver)
        signinpage.getunamefield().send_keys("rojalinadhall")
        time.sleep(4)
        signinpage.getpwdfield().send_keys("Swosti28102016")
        #signinpage.getcheckbox().click()
        time.sleep(4)
        signinpage.getSubmitBtn().click()
        time.sleep(6)

        mainpage = MainPage(self.driver)
        mainpage.getPopupWindow()
        mainpage.getOkayButton().click()
        #csigninpage.getSubmitBtn().click()
        self.getlogger()











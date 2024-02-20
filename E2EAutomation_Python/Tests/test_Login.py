import time

import pytest
import pytest_html

from PageObjects.HomePage import HomePage
from PageObjects.SignInPage import SignInPage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestFive(BaseClass):

    def test_Login(self, getData):

        homepage = HomePage(self.driver)
        time.sleep(6)
        homepage.getLoginBtn().click()
        homepage.getSignInBtn().click()

        signinpage = SignInPage(self.driver)
        signinpage.getunamefield().send_keys(getData["Username"])
        signinpage.getpwdfield().send_keys(getData["Password"])
        signinpage.getSubmitBtn().click()

        self.getlogger()

    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self, request):
        return request.param

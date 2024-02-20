import time

from PageObjects.ChildMenuPage import ChildMenuPage
from PageObjects.HomePage import HomePage
from PageObjects.ParentMenuPage import ParentMenuPage
from PageObjects.ResultPage import ResultPage
from PageObjects.SearchDomainPage import SearchDomainPage
from Utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_captureMenu(self):
        homepage = HomePage(self.driver)
        homepage.getMenuBtn().click()

        parentmenupage = ParentMenuPage(self.driver)
        parentlinks = parentmenupage.getParentMenuLinks()
        num = 1
        print("Parent-Menu---")
        print()
        for link in parentlinks:
            assert link.text
            print(num, "-->", link.text)
            num += 1

        parentmenupage.getParentDomainName().click()

        childmenupage = ChildMenuPage(self.driver)
        childlinks = childmenupage.getChildMenuLinks()
        #time.sleep(4)
        nums = 1
        print("Child-Menu---->")
        print()
        for childlink in childlinks:
            print(nums, "---->", childlink.text)
            time.sleep(2)
            nums += 1

        childmenupage.getChildDomainName().click()
        searchdomainpage = SearchDomainPage(self.driver)
        #time.sleep(2)
        str1 = "rojalinadhall.com"
        str2 = "ndtv.com"
        #searchdomainpage.getSearchDomain().send_keys(str1)
        searchdomainpage.getSearchDomain().send_keys(str2)
        #time.sleep(4)

        searchdomainpage.getSearchButton().click()


        resultpage = ResultPage(self.driver)
        #time.sleep(4)
        #assert resultpage.getResultText1().text == "Your domain is available!"
        assert resultpage.getResultText2().text == "ndtv.com is taken"

        #time.sleep(4)

        self.getlogger()


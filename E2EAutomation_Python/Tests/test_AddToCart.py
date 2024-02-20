import time

from PageObjects.BuyDomainPage import BuyDomainPage
from PageObjects.CartEmptyPage import CartEmptyPage
from PageObjects.DomainSpecsPage import DomainSpecsPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    def test_addtocart(self):
        homepage = HomePage(self.driver)
        homepage.getCartBtn().click()

        cartemptypage = CartEmptyPage(self.driver)
        print(cartemptypage.getMsgEmptyCart().text)
        #assert cartemptypage.getMsgEmptyCart().text == "There are no items in your basket"
        cartemptypage.getMsgShopping().click()

        #homepage.getDomainSearchField().send_keys("rojalina.com" + "\n")
        homepage.getDomainSearchField().send_keys("rojalina.com")
        #homepage.getDomainSearchField().click()
        homepage.getSearchButton().click()

        buydomainpage = BuyDomainPage(self.driver)
        print(buydomainpage.getSuccessTxt().text)

        buydomainpage.getDomainBtn().click()
        time.sleep(4)
        buydomainpage.getGoToCart().click()

        domainspecspage = DomainSpecsPage(self.driver)
        domainspecspage.getGoToCartBtn().click()

        self.getlogger()


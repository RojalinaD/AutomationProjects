from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestFour(BaseClass):

    def test_captureReviews(self):
        homepage = HomePage(self.driver)
        review_list = homepage.getReviewsTxt()
        #print(review_list[0].text)
        ind = 0
        num = 1
        while ind < 11:
            print(num, '--->', review_list[ind].text, '\n')
            ind += 1
            num += 1

        self.getlogger()



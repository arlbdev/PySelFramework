import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)

        homePage.getNameField().send_keys(getData["firstName"])
        homePage.getEmailField().send_keys(getData["email"])
        homePage.getSampleCheckBox().click()
        self.selectOptionByText(homePage.getGenderForm(), getData["gender"])

        homePage.getSubmitFormBtn().click()

        alertText = homePage.getSuccessMessageTxt().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

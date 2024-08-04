import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()

        homePage = HomePage(self.driver)

        log.info("Entering first name: " + getData["firstName"])
        homePage.getNameField().send_keys(getData["firstName"])

        log.info("Entering email address: " + getData["email"])
        homePage.getEmailField().send_keys(getData["email"])

        homePage.getSampleCheckBox().click()

        log.info("Choosing gender: " + getData["gender"])
        self.selectOptionByText(homePage.getGenderForm(), getData["gender"])

        log.info("Submitting form...")
        homePage.getSubmitFormBtn().click()

        alertText = homePage.getSuccessMessageTxt().text
        log.info("Form submitted with message: " + alertText)

        assert ("Success" in alertText)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

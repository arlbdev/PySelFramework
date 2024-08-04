import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)

        homePage.getNameField().send_keys(getData[0])
        homePage.getEmailField().send_keys(getData[1])
        homePage.getSampleCheckBox().click()
        self.selectOptionByText(homePage.getGenderForm(), getData[2])

        homePage.getSubmitFormBtn().click()

        alertText = homePage.getSuccessMessageTxt().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[("Juan", "juandelacruz@gmail.com", "Male"), ("Jane", "janedoe@gmail.com", "Female")])
    def getData(self, request):
        return request.param
from selenium.webdriver.support.select import Select
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)

        homePage.getNameField().send_keys("Juan")
        homePage.getEmailField().send_keys("juandelacruz@gmail.com")
        homePage.getSampleCheckBox().click()
        self.selectOptionByText(homePage.getGenderForm(), "Male")

        homePage.getSubmitFormBtn().click()

        alertText = homePage.getSuccessMessageTxt().text

        assert ("Success" in alertText)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        checkOutPage = CheckOutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)

        homePage.shopItems().click()
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getAddToCartBtn()[i].click()

        checkOutPage.getCheckoutButton().click()

        confirmPage.getConfirmCheckoutBtn().click()
        confirmPage.getCountryInputField().send_keys(confirmPage.countrySearchKey)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(confirmPage.countryLink)
        )
        confirmPage.getCountryLink().click()
        confirmPage.getTncCheckBox().click()
        confirmPage.getPurchaseBtn().click()
        textResult = confirmPage.getTextResult().text

        assert ("Success! Thank you!" in textResult)
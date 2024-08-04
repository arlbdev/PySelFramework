from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)

        checkOutPage = homePage.shopItems()

        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getAddToCartBtn()[i].click()

        confirmPage = checkOutPage.clickCheckOutButton()

        confirmPage.getConfirmCheckoutBtn().click()
        confirmPage.getCountryInputField().send_keys(confirmPage.countrySearchKey)
        self.verifyLinkPresence(confirmPage.countryName)
        confirmPage.getCountryLink().click()
        confirmPage.getTncCheckBox().click()
        confirmPage.getPurchaseBtn().click()
        textResult = confirmPage.getTextResult().text

        assert ("Success! Thank you!" in textResult)
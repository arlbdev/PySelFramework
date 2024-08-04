from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.clickShopItems()

        log.info("Getting all card titles...")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getAddToCartBtn()[i].click()

        confirmPage = checkOutPage.clickCheckOutButton()

        confirmPage.getConfirmCheckoutBtn().click()

        log.info(f"Entering country name as '{confirmPage.countrySearchKey}'...")
        confirmPage.getCountryInputField().send_keys(confirmPage.countrySearchKey)

        log.info("Verifying country name's existence...")
        self.verifyLinkPresence(confirmPage.countryName)

        confirmPage.getCountryLink().click()
        log.info("Selecting matching country...")

        confirmPage.getTncCheckBox().click()
        log.info("Checked terms and conditions...")

        confirmPage.getPurchaseBtn().click()
        log.info("Confirming purchase...")

        textResult = confirmPage.getTextResult().text

        result = "Success! Thank you!" in textResult

        if result:
            log.info(f"Result: {textResult}")
        else:
            log.error("Result: An error has occurred. Please try again.")

        assert result



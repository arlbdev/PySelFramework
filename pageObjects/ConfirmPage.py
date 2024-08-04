from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    confirmCheckoutBtn = (By.XPATH, "//button[@class='btn btn-success']")
    countryInputField = (By.ID, "country")
    countrySearchKey = "united"
    countryName = "United States of America"
    countryLink = (By.LINK_TEXT, "United States of America")
    tncCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.CSS_SELECTOR, "[type='submit']")
    textResult = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getConfirmCheckoutBtn(self):
        return self.driver.find_element(*ConfirmPage.confirmCheckoutBtn)

    def getCountryInputField(self):
        return self.driver.find_element(*ConfirmPage.countryInputField)

    def getCountryLink(self):
        return self.driver.find_element(*ConfirmPage.countryLink)

    def getTncCheckBox(self):
        return self.driver.find_element(*ConfirmPage.tncCheckbox)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getTextResult(self):
        return self.driver.find_element(*ConfirmPage.textResult)
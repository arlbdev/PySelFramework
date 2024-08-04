from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    addToCartBtn = (By.CSS_SELECTOR, ".card-footer button")
    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getAddToCartBtn(self):
        return self.driver.find_elements(*CheckOutPage.addToCartBtn)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutBtn)


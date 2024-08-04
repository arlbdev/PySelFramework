from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    sampleCheckbox = (By.ID, "exampleCheck1")
    genderForm = (By.ID, "exampleFormControlSelect1")
    submitFormBtn = (By.XPATH, "//input[@value='Submit']")
    successMessageTxt = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getNameField(self):
        return self.driver.find_element(*HomePage.name)

    def getEmailField(self):
        return self.driver.find_element(*HomePage.email)

    def getSampleCheckBox(self):
        return self.driver.find_element(*HomePage.sampleCheckbox)

    def getGenderForm(self):
        return self.driver.find_element(*HomePage.genderForm)

    def getSubmitFormBtn(self):
        return self.driver.find_element(*HomePage.submitFormBtn)

    def getSuccessMessageTxt(self):
        return self.driver.find_element(*HomePage.successMessageTxt)












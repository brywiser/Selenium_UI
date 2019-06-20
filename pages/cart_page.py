from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    #save = //*[contains(@class,'sc-product-title')][contains(text(), 'Koolkatkoo')]
    shopping_cart_text = (By.XPATH, "//h2[contains(text(),'Shopping Cart')]")
    checkout_button = (By.NAME, 'proceedToCheckout')

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element(self.shopping_cart_text)
        self.wait_for_element(self.checkout_button)

    def confirm_cart_items(self, item):
        locator = (By.XPATH, "//*[contains(@class,'sc-product-title')][contains(text(),\"" + item + "\")]")
        item_text = self.wait_for_element(locator).text
        error = ''
        if item not in item_text:
            error = "Wrong item added to cart, or not in cart: " + item_text
            return error
        return error

    def remove_cart_item(self, item):
        locator = (By.XPATH, "//input[@value='Delete'][contains(@aria-label, \"" + item + "\")]")
        self.wait_for_element(locator).click()

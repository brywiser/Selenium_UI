from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    product_title = (By.ID, 'productTitle')
    add_to_cart = (By.ID, 'add-to-cart-button')
    decline_warranty = (By.XPATH, "//button[@class='a-button-text'][contains(text(),'No Thanks')]")
    cart_button = (By.XPATH, "//input[@class='a-button-input'][@aria-labelledby='attach-sidesheet-view-cart-button-announce']")
    added_to_cart_slideout = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button-announce']")
    added_to_cart_heading_text = 'Cart'
    protection_plan = (By.XPATH, "//strong[.='4 Year Office Equipment Protection Plan']")

    def __init__(self, driver):
        self.driver = driver
        self.product_title_text = self.wait_for_element(self.product_title).text
        self.wait_for_element(self.add_to_cart)

    def assert_correct_product(self, item):
        errors = []
        if item not in self.product_title_text:
            errors.append("Wrong Product Page: " + self.product_title_text + " Expected: " + item)
        else:
            return errors
        return errors

    def add_item_to_cart(self, item):
        self.wait_for_element(self.add_to_cart).click()
        if item == 'ASUS MG28UQ 4K/UHD 28-Inch':
            self.wait_for_element(self.protection_plan)
            no_thanks = self.wait_for_element(self.decline_warranty)
            no_thanks.click()
        if item == 'Koolkatkoo Cute Ceramic Cat Coffee Mug 12 oz Cat Lovers Kitty Tea Mugs Gifts for Women Girls Black …':
            self.take_screenshot("Crazy_Cat_Cup.png")

    def click_slideout_menu_close(self):
        self.wait_for_element(self.cart_button).click()
        self.wait_for_element(self.amazon_logo).click()
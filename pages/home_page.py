from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage


class HomePage(BasePage):
    amazon_logo_id = (By.ID, 'nav-logo')
    product_banner_id = (By.ID, 'desktop-banner')
    first_sign_in_text = 'Sign in for the best experience'
    cart = (By.ID, 'nav-cart')

    def __init__(self, driver, item):
        self.driver = driver
        self.item = item
        self.wait_for_element(self.amazon_logo_id)
        self.wait_for_element(self.product_banner_id)

    def search_amzn(self):
        self.fill_field_by(self.search_box, self.item)
        self.wait_for_element(self.search_button).click()
        return SearchResultsPage(self.driver)

    def click_cart(self):
        self.wait_for_element(self.cart).click()
        return CartPage(self.driver)

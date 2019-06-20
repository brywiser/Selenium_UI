from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage

class SearchResultsPage(BasePage):
    search_results_grid = (By.XPATH, "//div[@class='s-result-list s-search-results sg-row']")
    results_found_text_id = (By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']")

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element(self.search_results_grid)
        self.results_found_text = self.wait_for_element(self.results_found_text_id).text
        self.expected_search_result_text = self.wait_for_element(self.search_box)

    def assert_correct_search_results(self):
        print(self.expected_search_result_text.get_attribute('value'))
        expected_search_result = "results for " + '"' + self.expected_search_result_text.get_attribute('value') + '"'
        print(expected_search_result)
        error = ''
        if expected_search_result not in self.results_found_text:
            error = "Not on search results page, or Wrong results appeared " + str(self.results_found_text)
            return error
        else:
            return error
    
    def click_product(self, item):
        product_result = (By.XPATH, "//span[contains(@class, 'a-text-normal')][contains(text(),\"" + item + "\")]")
        self.wait_for_element(product_result).click()
        return ProductPage(self.driver)
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import *
from selenium import webdriver

class BasePage(object):
    search_box = (By.ID, 'twotabsearchtextbox')
    search_button = (By.XPATH, "//input[@class='nav-input'][@value='Go']")
    amazon_logo = (By.XPATH, "//a[@class='nav-logo-link'][@aria-label='Amazon']")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(EC.visibility_of_element_located((locator[0], locator[1])))
        except TimeoutException:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('screenshot-%s.png' % now)
            assert False, "could not find element " + str(locator[1])
        else:
            elem = self.driver.find_element(locator[0], locator[1])
            return elem

    def fill_field_by(self, locator, input_text):
        elem = self.wait_for_element(locator)
        elem.send_keys(input_text)
    
    def take_screenshot(self, title):
        self.driver.get_screenshot_as_file(title)

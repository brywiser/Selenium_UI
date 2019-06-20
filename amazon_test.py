import pytest
from selenium import webdriver
from os.path import abspath
from pages.home_page import HomePage
import platform

USER_HOME = abspath(".")

def test_amazon():
    #Start Webdriver
    if platform.system() == "Darwin":
        driver = webdriver.Chrome(USER_HOME + "/chromedriver/chromedriver_mac")
    elif platform.system() == "Windows":
        driver = webdriver.Chrome(USER_HOME + "/chromedriver/chromedriver.exe")
    else:
        assert False, "Unrecognized OS"
    driver.get("http://www.amazon.com")
    items = ['ASUS MG28UQ 4K/UHD 28-Inch', "Metasploit: The Penetration Tester's Guide", 'Koolkatkoo Cute Ceramic Cat Coffee Mug 12 oz Cat Lovers Kitty Tea Mugs Gifts for Women Girls Black …']

    for item in items:
        #Initialize the homepage, will fail if certain elems are not found
        home_page = HomePage(driver, item)
        #search amazon for products
        search_results_page = home_page.search_amzn()
        #assert we are on the correct results page
        assert '' == search_results_page.assert_correct_search_results()
        #Find and Click the item
        product_page = search_results_page.click_product(item)
        #Assert the correct product page
        assert [] == product_page.assert_correct_product(item)
        #Add Item to cart
        product_page.add_item_to_cart(item)
        #Refresh to Amazon.com
        driver.get("http://www.amazon.com")

    #Confirm Cart is Correct
    cart_page = home_page.click_cart()
    for item in items:
        cart_page.confirm_cart_items(item)

    #Remove Monitor from cart
    cart_page.remove_cart_item(items[0])
    items.pop(0)

    #Reconfirm Items in cart
    for item in items:
        cart_page.confirm_cart_items(item)
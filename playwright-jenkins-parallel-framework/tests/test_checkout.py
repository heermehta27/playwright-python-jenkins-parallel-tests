from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

@pytest.fixture(autouse=True)
def setup_login_and_cart(page: Page):
    """Logs in and adds an item to the cart before each test in this module."""
    # Login
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    # Add item to cart
    cart_page = CartPage(page)
    cart_page.add_product_to_cart("Sauce Labs Backpack")
    cart_page.go_to_cart()

def test_successful_checkout(page: Page):
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    
    # Proceed to checkout from cart
    cart_page.proceed_to_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    
    # Fill information and continue
    checkout_page.fill_checkout_information("John", "Doe", "12345")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    
    # Finish checkout
    checkout_page.finish_checkout()
    
    # Assert checkout complete
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    assert checkout_page.get_complete_message() == "Thank you for your order!"

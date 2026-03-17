from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

@pytest.fixture(autouse=True)
def setup_login(page: Page):
    """Logs in before each test in this module."""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_add_product_to_cart(page: Page):
    cart_page = CartPage(page)
    
    # Add an item to the cart
    cart_page.add_product_to_cart("Sauce Labs Backpack")
    
    # Assert cart badge updates to 1
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

def test_view_cart_items(page: Page):
    cart_page = CartPage(page)
    
    # Add multiple items to the cart
    cart_page.add_product_to_cart("Sauce Labs Backpack")
    cart_page.add_product_to_cart("Sauce Labs Bike Light")
    
    # Navigate to the cart page
    cart_page.go_to_cart()
    
    # Assert URL and items count
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    assert cart_page.get_cart_items_count() == 2

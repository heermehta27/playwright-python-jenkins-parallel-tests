from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    # Assert successful login by checking the URL and a specific element
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_failed_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("locked_out_user", "secret_sauce")
    
    # Assert error message
    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_message
    
def test_invalid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "wrong_password")
    
    # Assert error message
    error_message = login_page.get_error_message()
    assert "Username and password do not match any user in this service" in error_message

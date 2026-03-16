from playwright.sync_api import Page
from utils.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navigate_to_login(self):
        self.navigate("/")
        
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

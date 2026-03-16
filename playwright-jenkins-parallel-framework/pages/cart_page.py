from playwright.sync_api import Page
from utils.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator(".cart_item")
        
    def add_product_to_cart(self, product_name: str):
        # Product name needs to be transformed to match the ID format (lowercase, spaces to hyphens)
        product_id = product_name.lower().replace(" ", "-")
        add_to_cart_btn = self.page.locator(f"[data-test='add-to-cart-{product_id}']")
        add_to_cart_btn.click()

    def go_to_cart(self):
        self.cart_link.click()

    def get_cart_items_count(self) -> int:
        return self.cart_items.count()

    def proceed_to_checkout(self):
        self.checkout_button.click()

from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self._header_title = page.locator(".title")
        self._inventory_item = page.locator(".inventory_item")
        


    def add_item_to_cart(self,item_name):
        """Finds an item by name and adds it to the cart"""
        item_to_add = self._inventory_item.filter(has_text=item_name)
        item_to_add.locator("button").click(timeout=5000)
        

    def get_total_items_in_cart(self):
        """Returns the total number of items in the cart"""
        return self.page.locator(".shopping_cart_badge").inner_text()



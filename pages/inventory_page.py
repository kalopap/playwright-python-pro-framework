from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self._header_title = page.locator(".title")

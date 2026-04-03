### Base page containing reusable methods for all pages

from playwright.sync_api import Page,expect

class BasePage:

    def __init__(self,page:Page):
        self.page = page

    def navigate_to(self,url):
        self.page.goto(url)

    def get_title(self):
        return self.page.locator("[data-test='title']")

from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)

        ##Login page locators
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button",name="Login")
        self._error_message = page.locator("[data-test='error']")

    def login(self,username,password):
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
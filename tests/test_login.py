
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect
import pytest
import allure


@allure.feature("Login Tests")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(page,test_data,env_config,get_full_url):
    """Test to verify that a standard user can login successfully."""

    #Setup
    login = LoginPage(page)
    inventory = InventoryPage(page)

    #Action
    with allure.step("Navigate to Home Page"):
        login.navigate_to(env_config["base_url"])
    
    with allure.step("Login as standard user"):
        login.login(test_data["users"]["standard"],env_config["password"])

    inventory_url = get_full_url("inventory")
    
    #Assert
    with allure.step("Verify that user is redirected to inventory page"):
        expect(page).to_have_url(inventory_url)
        expect(inventory.get_title()).to_have_text(test_data["header_titles"]["inventory"])

@pytest.mark.smoke
def test_invalid_login_error(page,test_data,env_config):
    #Setup
    login = LoginPage(page)

    login.navigate_to(env_config["base_url"])
    login.login(test_data["users"]["invalid"],env_config["password"])

    ##Error
    expect(login._error_message).to_be_visible()
    expect(login._error_message).to_have_text(test_data["error_messages"]["invalid_msg"])

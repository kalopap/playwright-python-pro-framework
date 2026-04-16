import pytest
import json
import os
from dotenv import load_dotenv
import allure

load_dotenv()

@pytest.fixture(scope="session")
def test_data():
    """Reads data from test.json file"""
    with open("data/testdata.json") as f:
        return json.load(f)
    
@pytest.fixture(scope="session")
def env_config():
    """Reads secrets and URLs from .env file"""
    return {
        "password": os.getenv("SAUCE_PASSWORD"),
        "base_url": os.getenv("BASE_URL")
    }

@pytest.fixture()
def get_full_url(env_config,test_data):
    """Combines base URL and endpoint to create full URL"""
    def _build_url(endpoint_key):
        return env_config["base_url"] + test_data["endpoints"][endpoint_key]
    return _build_url

@pytest.fixture
def setup_inventory(page,test_data,env_config):
    """ Log in to the inventory page"""
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate_to(env_config["base_url"])
    login.login(test_data["users"]["standard"],env_config["password"])


@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

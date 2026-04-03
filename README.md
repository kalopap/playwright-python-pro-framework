# SauceDemo Playwright Python Framework

A professional-grade automation framework using Playwright, Pytest, and the Page Object Model (POM).

## Features
- **POM Architecture**: Clean separation of locators and test logic.
- **Data-Driven**: Usernames and endpoints managed via JSON.
- **Secure**: Credentials managed via environment variables (`.env`).
- **Reporting**: Integrated with Allure and Pytest-HTML.
  
## 🏗️ Architecture Decisions

* **Centralized URL Factory:** Utilizes a custom Pytest fixture to dynamically construct URLs from environment configs and JSON endpoints, ensuring zero string-concatenation in test scripts.
* **Decoupled Data:** Test users and expected UI strings are stored in `data/test_data.json` to allow for easy maintenance without touching core logic.
* **Security First:** Implements a `.env` strategy to ensure sensitive credentials never reach the version control system.
* **Page Object Model (POM):** Pure separation of UI locators and test execution logic for high maintainability.

  
## Setup
1. Clone the repo.
2. Create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Install browsers: `playwright install`.
5. Create a `.env` file with `BASE_URL` and `SAUCE_PASSWORD`.

## Running Tests
Tests run in **Headless Chromium** by default for maximum CI speed and stability.

### Local Execution
To run across all browsers locally:
```bash
pytest --browser chromium --browser firefox --browser webkit
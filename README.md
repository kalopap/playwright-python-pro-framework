# SauceDemo Playwright Python Framework

A professional-grade automation framework using Playwright, Pytest, and the Page Object Model (POM).

## Features
- **POM Architecture**: Clean separation of locators and test logic.
- **Data-Driven**: Usernames and endpoints managed via JSON.
- **Secure**: Credentials managed via environment variables (`.env`).
- **Reporting**: Integrated with Allure and Pytest-HTML.

## Setup
1. Clone the repo.
2. Create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Install browsers: `playwright install`.
5. Create a `.env` file with `BASE_URL` and `SAUCE_PASSWORD`.

## Running Tests
Run all tests across multiple browsers:
```bash
pytest
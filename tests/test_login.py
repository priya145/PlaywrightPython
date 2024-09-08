import allure
from playwright.sync_api import sync_playwright
from pages.login import Login
from pages.testcasebase import BasePage
from testdata import loginData

# This is a test for Logging in with valid credentials
# Author - Priya Tayade
# Date - 08/09/2024
@allure.feature('User Login')
@allure.story('Login Functionality')
def test_user_login():
    test = Login()
    base = BasePage()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True to run tests headlessly
        page = browser.new_page()

        try:
            # Navigate to the login page
            test.getURL(page, loginData.url)

            # Login with Credentials
            test.login(page)

            # Verify successful login by checking the presence of a user-specific element
            test.isHeadingVisible(page)

        except AssertionError as e:
            # Generate Report
            base.generateReport(page)
            raise e  # Re-raise the exception to ensure the test fails

        finally:
            # Close browser
            browser.close()



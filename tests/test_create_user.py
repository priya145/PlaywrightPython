import allure
from playwright.sync_api import sync_playwright

from pages.createUser import CreateUser
from pages.login import Login
from pages.testcasebase import BasePage
from pages.userSearch import UserSearch
from testdata import loginData

# This is a test class for creating new user
# Author - Priya Tayade
# Date - 08/09/2024
@allure.feature('User Management')
@allure.story('Add New User Functionality')
def test_create_user():
    test = Login()
    base = BasePage()
    admin = UserSearch()
    user = CreateUser()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        page = browser.new_page()

        try:
            # Step 1: Login to the application
            test.getURL(page, loginData.url)  # Wait for 2 seconds to observe the page load

            # Login with valid credentials
            user.login(page)

            # Step 2: Navigate to the "Admin" section (User Management)
            admin.clickAdminSection(page, loginData.adminSection)

            # Step 3: Add a new user and fill the details
            user.addUser(page)

            # Step 5: Save the new user
            user.saveUser(page)

            # Step 6: Verify that the user was added successfully by searching for the username
            user.verifyUserAdded(page)

            # Check if the newly added user is in the search results
            assert loginData.random_username.lower() in page.text_content(loginData.searchResult).lower()

        except AssertionError as e:
            # Generate Report
            base.generateReport(page)
            raise e  # Re-raise to ensure test fails

        finally:
            # Close browser
            browser.close()

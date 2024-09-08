import allure
from playwright.sync_api import sync_playwright

from pages.login import Login
from pages.testcasebase import BasePage
from pages.userSearch import UserSearch
from testdata import loginData

# This is a test for searching existing user
# Author - Priya Tayade
# Date - 08/09/2024
@allure.feature('User Management')
@allure.story('Search User Functionality')
def test_user_search():
    test = Login()
    base = BasePage()
    admin = UserSearch()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        page = browser.new_page()

        try:
            # Step 1: Login to the application
            test.getURL(page, loginData.url)

            # Login with valid credentials
            admin.login(page)

            # Step 2: Navigate to the "Admin" section (User Management)
            admin.clickAdminSection(page)

            # Wait for the search bar to become visible
            admin.isSearchVisible(page)

            # Step 3: Perform a search for the user 
            admin.searchUser(page)

            # Step 4: Verify that search results are displayed
            admin.isSearchVisible(page)
            # Check if search results contain the search keyword
            assert loginData.search_query.lower() in page.text_content(loginData.searchResult).lower()

            # Step 5: Validate that the user details page can be opened and check if user is visible from search results
            admin.openUserPage(page)  # Click on the first user in the results

        except AssertionError as e:
            # Generate Report
            base.generateReport(page)
            raise e  # Re-raise to ensure test fails

        finally:
            # Close browser
            browser.close()

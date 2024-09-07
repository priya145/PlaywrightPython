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
            test.takeUsername(page, loginData.username, "Admin")
            test.takePassword(page, loginData.password, "admin123")

            # Click on the "Login" button
            test.clickLogin(page, loginData.submit)
            test.isVisible(page, loginData.heading)

            # Step 2: Navigate to the "Admin" section (User Management)
            admin.clickAdminSection(page, loginData.adminSection)

            # Wait for the search bar to become visible
            admin.isSearchVisible(page, loginData.search)

            # Step 3: Perform a search for the user 
            admin.takeSearchInput(page, loginData.search, loginData.search_query)
            test.clickLogin(page, loginData.submit)

            # Step 4: Verify that search results are displayed
            admin.isSearchVisible(page, loginData.searchResult)
            # Check if search results contain the search keyword
            assert loginData.search_query.lower() in page.text_content(loginData.searchResult).lower()

            # Step 5: Validate that the user details page can be opened from search results
            admin.openUserPage(page,loginData.userPage)  # Click on the first user in the results

            # Check if the user details page is opened
            admin.isUserDetailVisible(page, loginData.userDetail)

        except AssertionError as e:
            # Generate Report
            base.generateReport(page)
            raise e  # Re-raise to ensure test fails

        finally:
            # Close browser
            browser.close()

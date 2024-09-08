import requests
import allure
from playwright.sync_api import sync_playwright

from pages.apiResponse import APIResponse
from pages.testcasebase import BasePage
from testdata import loginData

API_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"


# Perform login using Playwright and extract session cookies
def get_auth_cookies():
    api = APIResponse()
    base = BasePage()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        page = browser.new_page()

        try:
            api.getURL(page, loginData.url)
            api.login(page)

            # Wait for the dashboard to load
            api.isHeadingVisible(page)

            # Extract cookies after login
            cookies = page.context.cookies()

            # Convert cookies to the format required by the requests library
            return base.coockieDict(cookies)

        finally:
            # Close the browser
            browser.close()


@allure.feature('API Testing')
@allure.story('Product Details API Testing')
def test_api_response():
    # Get authentication cookies using Playwright
    cookies = get_auth_cookies()
    api = APIResponse()
    base = BasePage()
    print(cookies)
    # Send a GET request to the API endpoint with authentication cookies
    response = requests.get(API_URL, cookies=cookies)
    print(response)

    # Verify that the response status code is 200
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Validate the structure of the response JSON
    json_data = response.json()
    print(json_data)
    base.validateJSON(json_data)



    # Verify the correctness of the data against the UI using Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        page = browser.new_page()

        try:
            # Step 5.1: Login to the application via UI
            api.getURL(page, loginData.url)
            api.login(page)

            # Wait for the dashboard to load
            api.isHeadingVisible(page)

            # Step 5.2: Navigate to the "Admin" section (User Management)
            api.navigateAdmin(page)

            # Fetch the list of users displayed on the UI
            users_ui = page.query_selector_all(loginData.listOfUser)

            # Step 5.3: Verify the correctness of data from API and UI
            for index, user in enumerate(users_ui):
                username_ui = user.query_selector(loginData.userNameUI).text_content().strip()
                role_ui = user.query_selector(loginData.roleUI).text_content().strip()
                status_ui = user.query_selector(loginData.statusUI).text_content().strip()

                # Fetch the same user from the API data
                user_api = json_data['data'][index]
                username_api = user_api['userName']
                role_api = user_api['userRole']['name']
                status_api = user_api['status']

                # Compare UI data with API data
                assert username_ui == username_api, f"Mismatch in username: {username_ui} != {username_api}"
                assert role_ui == role_api, f"Mismatch in role: {role_ui} != {role_api}"
    #           assert status_ui == status_api, f"Mismatch in status: {status_ui} != {status_api}"

        except Exception as e:
            # Capture screenshot on failure
            base.generateReport(page)
            raise e

        finally:
            # Close browser
            browser.close()

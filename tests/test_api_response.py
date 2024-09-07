import requests
import allure
from playwright.sync_api import sync_playwright

API_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"


# Step 1: Perform login using Playwright and extract session cookies
def get_auth_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        page = browser.new_page()

        try:
            # Navigate to login page
            page.goto('https://opensource-demo.orangehrmlive.com')
            page.fill('input[name="username"]', 'Admin')
            page.fill('input[name="password"]', 'admin123')
            page.click('button[type="submit"]')

            # Wait for the dashboard to load to ensure login is successful
            page.wait_for_selector('h6', state='visible')

            # Extract cookies after login
            cookies = page.context.cookies()

            # Convert cookies to the format required by the requests library
            cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}

            return cookie_dict

        finally:
            # Close the browser
            browser.close()


@allure.feature('API Testing')
@allure.story('Product Details API Testing')
def test_api_response():
    # Step 1: Get authentication cookies using Playwright
    cookies = get_auth_cookies()

    # Step 2: Send a GET request to the API endpoint with authentication cookies
    response = requests.get(API_URL, cookies=cookies)

    # Step 3: Verify that the response status code is 200
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Step 4: Validate the structure of the response JSON
    json_data = response.json()

    assert 'data' in json_data, "'data' key is missing in response"
    assert isinstance(json_data['data'], list), "'data' should be a list of users"

    for user in json_data['data']:
        assert 'userName' in user, "Missing 'userName' in user data"
        assert 'status' in user, "Missing 'status' in user data"
        assert 'userRole' in user, "Missing 'userRole' in user data"

    # Step 5: Verify the correctness of the data against the UI using Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless execution
        page = browser.new_page()

        try:
            # Step 5.1: Login to the application via UI
            page.goto('https://opensource-demo.orangehrmlive.com')
            page.fill('input[name="username"]', 'Admin')
            page.fill('input[name="password"]', 'admin123')
            page.click('button[type="submit"]')

            # Wait for the dashboard to load
            page.wait_for_selector('h6', state='visible')
            page.wait_for_timeout(2000)

            # Step 5.2: Navigate to the "Admin" section (User Management)
            page.click('a[href="/web/index.php/admin/viewAdminModule"]')
            page.wait_for_timeout(2000)

            # Fetch the list of users displayed on the UI
            users_ui = page.query_selector_all('div[class*="oxd-table-body"] div[class*="oxd-table-row"]')

            # Step 5.3: Verify the correctness of data from API and UI
            for index, user in enumerate(users_ui):
                username_ui = user.query_selector('div:nth-child(2)').text_content().strip()
                role_ui = user.query_selector('div:nth-child(3)').text_content().strip()
                status_ui = user.query_selector('div:nth-child(5)').text_content().strip()

                # Fetch the same user from the API data
                user_api = json_data['data'][index]
                username_api = user_api['userName']
                role_api = user_api['userRole']['name']
                status_api = user_api['status']

                # Compare UI data with API data
                assert username_ui == username_api, f"Mismatch in username: {username_ui} != {username_api}"
                assert role_ui == role_api, f"Mismatch in role: {role_ui} != {role_api}"
                assert status_ui == status_api, f"Mismatch in status: {status_ui} != {status_api}"

        except Exception as e:
            # Capture screenshot on failure
            screenshot_path = 'C:/Learning/pythonProject/screenshots/screenshot_failure_api_ui_verification.png'
            page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name='Failure Screenshot')
            raise e

        finally:
            # Close browser
            browser.close()

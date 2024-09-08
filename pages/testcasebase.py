import time
import allure
from playwright.async_api import Page

# This is a Base class having playwright core methods
# Author - Priya Tayade
# Date - 08/09/2024
class BasePage:
    def getURL(self, page: Page, url):
        page.goto(url)
        time.sleep(2)

    def getInput(self, page: Page, locator, input):
        page.fill(locator, input)
        time.sleep(1)

    def clickButton(self, page: Page, locator):
        page.click(locator)
        time.sleep(3)

    def isVisible(self, page: Page, locator):
        page.wait_for_selector(locator, state='visible')
        assert page.is_visible(locator)  # Assumes that after login a heading 'Dashboard' is visible
        time.sleep(3)

    def listOfInput(self, page: Page, locator):
        return page.query_selector_all(locator)

    def generateReport(self, page: Page):
        screenshot_path = 'C:/Learning/pythonProject/screenshots/screenshot_failure.png'
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name='Failure Screenshot')

    def coockieDict(self, cookies):
        cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
        return cookie_dict

    def validateJSON(selfself, json_data):
        assert 'data' in json_data, "'data' key is missing in response"
        assert isinstance(json_data['data'], list), "'data' should be a list of users"

        for user in json_data['data']:
            assert 'userName' in user, "Missing 'userName' in user data"
            assert 'status' in user, "Missing 'status' in user data"
            assert 'userRole' in user, "Missing 'userRole' in user data"

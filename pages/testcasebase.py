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

    def generateReport(self, page: Page):
        screenshot_path = 'C:/Learning/pythonProject/screenshots/screenshot_failure.png'
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name='Failure Screenshot')


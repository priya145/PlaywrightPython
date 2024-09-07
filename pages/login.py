from playwright.sync_api import Page
from pages.testcasebase import BasePage

# This is Page object class for login functionality
# Author - Priya Tayade
# Date - 08/09/2024
class Login(BasePage):
    def getURL(self, page: Page, url):
        base = BasePage()
        base.getURL(page, url)

    def takeUsername(self, page: Page, locator, text):
        base = BasePage()
        base.getInput(page, locator, text )

    def takePassword(self, page: Page, locator, text):
        base = BasePage()
        base.getInput(page, locator, text)

    def clickLogin(self, page: Page, locator):
        base = BasePage()
        base.clickButton(page, locator)

    def isHeadingVisible(self, page: Page, locator):
        base = BasePage()
        base.isVisible(page, locator)
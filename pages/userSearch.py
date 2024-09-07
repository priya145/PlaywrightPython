from playwright.sync_api import Page
from pages.testcasebase import BasePage

# This is Page object class for User Search functionality
# Author - Priya Tayade
# Date - 08/09/2024
class UserSearch(BasePage):

    def takeUsername(self, page: Page, locator, text):
        base = BasePage()
        base.getInput(page, locator, text )

    def takeSearchInput(self, page: Page, locator, text):
        base = BasePage()
        base.getInput(page, locator, text)

    def clickAdminSection(self, page: Page, locator):
        base = BasePage()
        base.clickButton(page, locator)

    def openUserPage(self, page: Page, locator):
        base = BasePage()
        base.clickButton(page, locator)

    def isSearchVisible(self, page: Page, locator):
        base = BasePage()
        base.isVisible(page, locator)

    def isUserDetailVisible(self, page: Page, locator):
        base = BasePage()
        base.isVisible(page, locator)
from playwright.sync_api import Page
from pages.testcasebase import BasePage

# This is Page object class for login functionality
# Author - Priya Tayade
# Date - 08/09/2024
from testdata import loginData


class APIResponse(BasePage):
    def getURL(self, page: Page, url):
        base = BasePage()
        base.getURL(page, url)

    def navigateAdmin(self, page: Page,):
        base = BasePage()
        base.clickButton(page, loginData.adminSection)

    def login(self, page: Page):
        base = BasePage()
        base.getInput(page, loginData.username, loginData.user)
        base.getInput(page, loginData.password, loginData.passcred)
        base.clickButton(page,loginData.submit)

    def isHeadingVisible(self, page: Page):
        base = BasePage()
        base.isVisible(page, loginData.heading)

    def getListOfUser(self, page: Page):
        base = BasePage()
        base.listOfInput(page, loginData.listOfUser)
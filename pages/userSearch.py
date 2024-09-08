from playwright.sync_api import Page
from pages.testcasebase import BasePage

# This is Page object class for User Search functionality
# Author - Priya Tayade
# Date - 08/09/2024
from testdata import loginData


class UserSearch(BasePage):

    def login(self, page: Page):
        base = BasePage()
        base.getInput(page, loginData.username, loginData.user)
        base.getInput(page, loginData.password,loginData.passcred)
        base.clickButton(page, loginData.submit)
        base.isVisible(page, loginData.heading)


    def searchUser(self, page: Page):
        base = BasePage()
        base.getInput(page, loginData.search, loginData.search_query)
        base.clickButton(page, loginData.submit)

    def clickAdminSection(self, page: Page):
        base = BasePage()
        base.clickButton(page, loginData.adminSection)

    def openUserPage(self, page: Page):
        base = BasePage()
        base.clickButton(page, loginData.userPage)
        base.isVisible(page,loginData.userDetail)

    def isSearchVisible(self, page: Page):
        base = BasePage()
        base.isVisible(page, loginData.search)

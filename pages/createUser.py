from playwright.sync_api import Page
from pages.testcasebase import BasePage
from testdata import loginData

# This is Page object class for Creating new user
# Author - Priya Tayade
# Date - 08/09/2024
class CreateUser(BasePage):
    def addUser(self, page: Page):
        base = BasePage()
        base.clickButton(page, loginData.addUser)
        base.clickButton(page, loginData.userRoleDropdown)
        base.clickButton(page, loginData.adminRole)
        base.clickButton(page, loginData.statusDropdown)
        base.clickButton(page, loginData.selectStatus)
        base.getInput(page, loginData.newUser, loginData.random_username)
        base.getInput(page, loginData.newPassword, loginData.passwordN)
        base.getInput(page, loginData.confirmPassword, loginData.passwordN)
        page.fill('input[placeholder="Type for hints..."]', loginData.employee_name)
        page.wait_for_selector(f'div[role="listbox"] div:has-text("{loginData.employee_name}")')
        page.click(f'div[role="listbox"] div:has-text("{loginData.employee_name}")')
        page.wait_for_timeout(1000)

    def saveUser(self, page: Page):
        base = BasePage()
        base.clickButton(page, loginData.submit)

    def verifyUserAdded(self, page: Page):
        base = BasePage()
        base.getInput(page, loginData.search, loginData.random_username)
        base.clickButton(page, loginData.submit)

    def login(self, page: Page):
        base = BasePage()
        base.getInput(page, loginData.username, loginData.user )
        base.getInput(page, loginData.password,loginData.passcred)
        base.clickButton(page, loginData.submit)
        base.isVisible(page, loginData.heading)

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
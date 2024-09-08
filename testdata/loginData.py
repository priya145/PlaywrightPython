import random

username = 'input[name="username"]'
url = "https://opensource-demo.orangehrmlive.com"
password = 'input[name="password"]'
submit = 'button[type="submit"]'
heading = 'h6'
user = 'Admin'
passcred = 'admin123'

adminSection = 'a[href="/web/index.php/admin/viewAdminModule"]'
search = 'input[placeholder="Search"]'
search_query = 'Admin'
searchResult = 'div[class*="oxd-table-body"]'
userPage = 'div[class*="oxd-table-body"] div:nth-child(1)'
userDetail = 'h6[class*="user-info-header"]'

addUser = "//button[text()=' Add ']"
userRoleDropdown = 'div[class*="oxd-select-text-input"]'
adminRole = 'div[role="listbox"] > div:has-text("Admin")'
statusDropdown = 'div[class*="oxd-select-text-input"] >> nth=1'
selectStatus = 'div[role="listbox"] > div:has-text("Enabled")'
newUser = 'input[name="username"]'
newPassword = 'input[name="password"]'
confirmPassword = 'input[name="confirmPassword"]'
passwordN = 'Qwerty123'
employeeName = 'Admin'
random_username = f'user_{random.randint(1000, 9999)}'

listOfUser = 'div[class*="oxd-table-body"] div[class*="oxd-table-row"]'
userNameUI = 'div:nth-child(2)'
roleUI = 'div:nth-child(3)'
statusUI = 'div:nth-child(5)'

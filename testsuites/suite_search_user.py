import pytest

# Test runner class to run without commands
def suite_search_user():
    # Run pytest with the --alluredir option to specify the directory for Allure results
    pytest.main([
        'C:/Learning/pythonProject/tests/test_user_search.py',         # Specify your test file
        '--alluredir=C:/Learning/pythonProject/allure-results'         # Specify the directory to store allure results
    ])

if __name__ == "__main__":
    suite_search_user()

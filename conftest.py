import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', 
        action='store', 
        default="chrome",
        help="Choose browser: chrome or firefox"
        )
    parser.addoption(
        '--language', 
        action='store', 
        default='ru',
        help='Choose language'
        )

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', 
            {'intl.accept_languages': user_language }
            )
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
        browser = None
    yield browser
    print("\nquit browser...")
    browser.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")
    # option to start tests without visible browser
    parser.addoption('--headless', action='store_true',
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    headless = request.config.getoption("headless")
    # add option to set in the browser language that get from command line for chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # add option not to show DevTools listening
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", language)
    # if option headless is added to command, start browser in headless (not visible) mode
    if headless:
        options.add_argument('--headless')
        options.add_argument("--window-size=1920x1080")
        options_firefox.add_argument('--headless')
        options_firefox.add_argument("--window-size=1920x1080")
    if browser_name == "chrome":
        # set added options to browser (chrome)
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
    
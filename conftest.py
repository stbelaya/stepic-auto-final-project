import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    language = request.config.getoption("language")
    # add option to set in the browser language that get from command line for chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # add option not to show DevTools listening
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # set added options to browser (chrome)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
    
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose language, for example: 'en', 'ru'")
    parser.addoption('--headless',
                     action='store',
                     default='true',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    headless = request.config.getoption('headless')

    if language:
        pass
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox, --language should be given")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        if headless == 'true':
            options.add_argument('headless')
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox, --language should be given")
    yield browser
    browser.quit()

#set up code, which every single selenium will be needing whenever we ran a selenium test

import pytest
from selenium import webdriver #in this case this webdriver is chrome so we'll import chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function") #fixture is a function that we attach to test, before the test run - Scope allows us to share fixtures across class, modules, functions...
def chrome_browser_instance(request):   #this builds instance of a browser, starts a browser so then we can run tests with other functions
    """
    provide a selenium webdriver instance
    """

    options = Options()
    options.headless = False #this being false will cause test not to be open a new page, if true it would do it in the background
    browser = webdriver.Chrome(chrome_options=options) 
    yield browser
    browser.close()
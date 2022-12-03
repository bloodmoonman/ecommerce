import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ...tests.selenium import chrome_browser_instance


@pytest.mark.selenium
def test_create_new_admin_user(create_admin_user): #adds the new user to the admin table
    assert create_admin_user.__str__() == "admin" #by default __str__ should equal the username, we just created

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, create_admin_user, chrome_browser_instance):
    #selenium requires a browser, so in order to test in browser it needs a browser
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url, "/admin/login/")))


    #selecting the inputs from the page, where user filled out.
    user_name = browser.find_element(By.NAME, "username") #using find_element to find the actual input field on the page, which user fills.
    user_password = browser.find_element(By.NAME, "password") #you can find the names by right clicking the page and finding that input's name in html.
    submit = browser.find_element(By.XPATH, "//input[@value='Log in']")

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source #checking if Site administration in the page source, because if it is in, then it means we are logged in



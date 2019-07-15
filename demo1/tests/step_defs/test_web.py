import _pytest.fixtures
from pytest_bdd import given, parsers, when, then, scenario
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

google_page = 'https://google.co.in'
file_path = '../features/web.feature'
# better not to hardcode the path, instead can be fetched using os.path


@_pytest.fixtures.fixture()
def browser():
    print('Initiating Chrome browser')
    browser_obj = webdriver.Chrome(ChromeDriverManager().install())
    return browser_obj


@scenario(file_path, 'Basic Google Search')
def test_google():
    """Basic google search"""


@given('The Google Search Page is displayed')
def gogoogle(browser):
    browser.get(google_page)


@when(parsers.parse('The user searches for {phrase}'))
def search_phrase(browser, phrase):
    browser.find_element_by_name('q').send_keys(phrase)
    browser.find_element_by_name('q').send_keys(Keys.RETURN)


@then(parsers.parse('the results are shown for {phrase}'))
def results_have_one(browser):
    xpath = '//a[starts-with(@href, "https://www.mozilla.org/en-US/firefox/new/")]'
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0


# Need to add a tear down fuction

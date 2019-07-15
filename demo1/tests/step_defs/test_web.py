import selenium, pytest, os, pytest_bdd , requests , parser
from pytest_bdd import given, parsers, scenarios, when, then, scenario

import pytest_bdd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

google_page = 'https://google.co.in'
#phrase_1 = 'Firefox Download'


@scenario('../features/web.feature','Basic Google Search')

@pytest.fixture
def browser():
    print('Initiating Chrome browser')
    b = webdriver.Chrome(ChromeDriverManager().install())
    #b = webdriver.chrom
    #b.implicitlywait(10)
    b.quit()


@given('Google homepage is displayed')
def gogoogle(browser, google_page):
    browser.get(google_page)

@when(parsers.parse('The user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    browser.find_element_by_name('q').send_keys(phrase)
    browser.find_element_by_name('q').send_keys(Keys.RETURN)

@then(parsers.parse('the results are shown for "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0



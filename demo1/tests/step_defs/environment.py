
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Hooks

# Firefox is the hard-coded browser of choice.
# Feel free to change it here.
# The correct browser and WebDriver executable must be installed on the test machine.
# A flexible framework would read the browser choice from inputs or config data.


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = webdriver.Firefox()
        context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()

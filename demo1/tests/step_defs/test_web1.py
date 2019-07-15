import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.co.in")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Firefox Install")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
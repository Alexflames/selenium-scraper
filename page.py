from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = MainPageLocators.FIND_MATCHING_STRING


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    
    def verify_loaded(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(MainPageLocators.DOWNLOAD_SIGN))
        element = self.driver.find_element(*MainPageLocators.DOWNLOAD_SIGN)
        print(element.text)
        
    def frame_switch(self, name_selector):
            self.driver.switch_to.frame(self.driver.find_element_by_name(name_selector))
        
    def __init__(self, driver):
        super().__init__(driver)
        self.frame_switch('x1')
        self.verify_loaded()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_find_matching_strings(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.FIND_MATCHING_STRING_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
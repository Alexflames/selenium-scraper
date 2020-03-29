from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from element import BasePageElement
from locators import MainPageLocators
from locators import SearchResultsPageLocators
from random import randint
from time import sleep
from time import time
import csv

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = MainPageLocators.FIND_MATCHING_STRING


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        
    def frame_switch(self, name_selector):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.NAME, name_selector)))
        self.driver.switch_to.frame(self.driver.find_element_by_name(name_selector))
        
    def return_to_default_frame(self):
        self.driver.switch_to.parent_frame()


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    
    def verify_loaded(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(MainPageLocators.DOWNLOAD_SIGN))
        #element = self.driver.find_element(*MainPageLocators.DOWNLOAD_SIGN)
        #print(element.text)
        
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
        
    def click_switch_to_context(self):
        self.return_to_default_frame()
        self.frame_switch('x2')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(MainPageLocators.WORD_CONTEXT))
        element = self.driver.find_element(*MainPageLocators.WORD_CONTEXT)
        element.click()
        self.return_to_default_frame()
        

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.frame_switch('x3')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(SearchResultsPageLocators.MORE_CONTEXT_LABEL))
        
    def cycle_through_pages(self, pages_count):
        with open('datares' + str(time()) + '.csv', 'w', newline='') as csvfile:
            context_writer = csv.writer(csvfile, delimiter='^',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            for i in range(pages_count):
                self.get_data(context_writer)
                self.go_and_wait()
        
    def get_data(self, writer):
        try:
            for element in self.driver.find_elements_by_tag_name('tr')[2:]:
                row = []
                for cell in element.find_elements_by_tag_name('td'):
                    row.append(cell.text)
                writer.writerow(row)
        finally:
            return
    
    def go_and_wait(self):
        navigation_arrow = self.driver.find_elements_by_tag_name('td')[0].find_elements_by_tag_name('a')[6]
        navigation_arrow.click()
        
        self.return_to_default_frame() # Now gow to main frame
        random_time = randint(3, 6)    # Wait random time. The page should reload
        print('i`m waiting', random_time, 'seconds')
        sleep(random_time)
        self.frame_switch('x3')
        pass
        
        
    
    
    
    
    
    
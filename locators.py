from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    FIND_MATCHING_STRING_BUTTON = (By.ID, 'submit1')
    DOWNLOAD_SIGN = (By.CLASS_NAME, 'pzz4') # used to verify that page is loaded
    FIND_MATCHING_STRING = (By.ID, 'p')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
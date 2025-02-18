import allure
import pytest
from selenium.webdriver.common.by import By
from src.test.python.navigationUtil.PageNavigationUtil import PageNavigationUtil
from src.main.core.Log import Log
from src.main.core.DriverWrapper import DriverWrapper
from src.main.core.elements.Input import Input

class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        Log.set_name("GoogleSearchTest")
        self.driver = DriverWrapper()

    @allure.story("Google Search")
    @allure.title("Search for Bosco Lviv")
    @allure.description("This test verifies the search functionality for 'bosco lviv' on Google.")
    def test_search_bosco_lviv(self):
        search_query = "bosco lviv"
        with allure.step("Navigate to Google main page"):
            PageNavigationUtil.toMainPage()
        
        with allure.step("Enter search query"):
            item = DriverWrapper.find_element(By.NAME, "q")
            input_element = Input(item)
            input_element.write(search_query)
        with allure.step("Submit search"):
            input_element.submit()

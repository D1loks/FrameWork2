import os
import sys

from src.main.core.elements.Input import Input

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

import pytest
from selenium.webdriver.common.by import By
from src.test.python.navigationUtil.PageNavigationUtil import PageNavigationUtil
from src.main.core.Log import Log
from src.main.core.DriverWrapper import DriverWrapper


class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        Log.set_name("GoogleSearchTest")
        self.driver = DriverWrapper()

    def test_search_bosco_lviv(self):
        search_query = "bosco lviv"
        PageNavigationUtil.toMainPage()
        input_element = Input(self.driver.find_element(By.NAME, "q"))
        input_element.write(search_query)
        input_element.submit()


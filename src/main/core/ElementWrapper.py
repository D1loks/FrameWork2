from typing import List

from selenium.webdriver.remote.webelement import WebElement

from AutomationWait import *
from DriverWrapper import *


class ElementWrapper:
    def __init__(self, base: WebElement, locator_type: str, locator_value: str):
        self.base = base
        self.locator_type = locator_type
        self.locator_value = locator_value

    def get_base(self) -> WebElement:
        return self.base

    def get_locator_info(self):
        return self.locator_type, self.locator_value

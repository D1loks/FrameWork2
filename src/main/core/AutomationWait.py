from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class AutomationWait:

    @staticmethod
    def wait_page_load(driver, timeout=100):
        driver.set_page_load_timeout(timeout)

    @staticmethod
    def wait_for_element_clickable(driver, element, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(element))

    @staticmethod
    def wait_for_element_visible(driver, element, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.visibility_of(element))

    @staticmethod
    def wait_visible_clickable(driver, element, timeout=10):
        visible_element = AutomationWait.wait_for_element_visible(driver, element, timeout)
        return AutomationWait.wait_for_element_clickable(driver, visible_element, timeout)

    @staticmethod
    def wait_title_contains(driver, title, timeout=10):
        WebDriverWait(driver, timeout).until(EC.title_contains(title))

    @staticmethod
    def wait(time_ms):
        time.sleep(time_ms / 1000)

    @staticmethod
    def wait_for_element_to_disappear(driver, element, timeout=10):
        WebDriverWait(driver, timeout).until(EC.invisibility_of_element(element))

    @staticmethod
    def wait_for_element_to_disappear_by_locator(driver, locator, timeout=10):
        WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))

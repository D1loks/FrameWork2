from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.main.core.Log import Log, LogType


class MyEventListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        Log.log(f"Намагаємось перейти на URL: {url}", LogType.INFO)

    def after_navigate_to(self, url, driver):
        Log.log(f"Успішно перейшли на URL: {url}", LogType.INFO)

    def before_click(self, element, driver):
        Log.log(f"Намагаємось клікнути на елемент: {element.tag_name}", LogType.INFO)

    def after_click(self, element, driver):
        Log.log(f"Успішно клікнули на елемент: {element.tag_name}", LogType.INFO)

    def before_change_value_of(self, element, driver):
        Log.log(f"Намагаємось змінити значення елемента: {element.tag_name}", LogType.INFO)

    def after_change_value_of(self, element, driver):
        Log.log(f"Успішно змінили значення елемента: {element.tag_name}", LogType.INFO)

    def on_exception(self, exception, driver):
        Log.log(f"Виникла помилка: {str(exception)}", LogType.ERROR)

class DriverWrapper:
    _driver = None
    _wait = None

    def __init__(self):
        if DriverWrapper._driver is None:
            driver_type = self.get_property("driver")
            if driver_type == "Chrome":
                chrome_service = ChromeService(ChromeDriverManager().install())
                base_driver = webdriver.Chrome(service=chrome_service)
            elif driver_type == "Firefox":
                firefox_service = FirefoxService(GeckoDriverManager().install())
                base_driver = webdriver.Firefox(service=firefox_service)
            else:
                raise ValueError(f"Unsupported driver type: {driver_type}")

            DriverWrapper._driver = EventFiringWebDriver(base_driver, MyEventListener())

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls()
        return cls._driver

    def get(self, url):
        """Метод для переходу на вказаний URL"""
        if self._driver is None:
            self.__init__()
        self._driver.get(url)

    @classmethod
    def find_element(self, by, value):
        """Метод для знаходження елемента"""
        #Log.log(f"Locator: {by} Value: {value}", LogType.INFO)
        return self.get_driver().find_element(by, value), by, value

    def find_elements(self, by, value):
        """Метод для знаходження списку елементів"""
        return (self.get_driver().find_elements(by, value), by, value)


    @classmethod
    def get_fluent_wait(cls):
        if cls._wait is None:
            cls._wait = WebDriverWait(cls.get_driver(), 30, poll_frequency=5, ignored_exceptions=[NoSuchElementException])
        return cls._wait

    @staticmethod
    def get_property(property_name):
        properties = {
            "driver": "Chrome"  # Замініть на реальне читання з файлу або змінної оточення
        }
        return properties.get(property_name, None)




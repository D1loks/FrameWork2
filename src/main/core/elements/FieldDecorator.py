from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class FieldDecorator:
    def __init__(self, search_context: WebDriver):
        """Приймає WebDriver як контекст пошуку."""
        self.search_context = search_context

    def decorate(self, locator_type: By, locator_value: str, element_class):
        """
        Додає об'єкт-обгортку для веб-елемента.

        :param locator_type: Тип локатора (By.CSS_SELECTOR, By.XPATH і т.д.)
        :param locator_value: Значення локатора
        :param element_class: Клас-обгортка (наприклад, Button)
        :return: Екземпляр об'єкта element_class
        """
        element = self.search_context.find_element(locator_type, locator_value)
        return element_class(element)

    def decorate_list(self, locator_type: By, locator_value: str, element_class):
        """
        Додає список об'єктів-обгорток для веб-елементів.

        :param locator_type: Тип локатора
        :param locator_value: Значення локатора
        :param element_class: Клас-обгортка
        :return: Список об'єктів element_class
        """
        elements = self.search_context.find_elements(locator_type, locator_value)
        return [element_class(el) for el in elements]

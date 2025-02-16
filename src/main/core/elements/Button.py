from selenium.webdriver.remote.webelement import WebElement

from src.main.core.Log import Log, LogType


class Button:
    def __init__(self, tuple):
        self.base = tuple[0]
        self.locator_type = tuple[1]
        self.locator_value = tuple[2]
        Log.log(f"Я Button знайдений за локатором: {self.locator_type} з значенням: {self.locator_value}", LogType.INFO)

    def click(self):
        Log.log(f"Я Button виконую дію - клік на кнопку з локатором: {self.locator_type}і значенням: {self.locator_value}", LogType.INFO)
        self.base.click()

    def get_text(self) -> str:
        Log.log(f"Я Button виконую дію - отримання тексту кнопки з локатором: {self.locator_type}і значенням: {self.locator_value}", LogType.INFO)
        return self.base.text

    def get_button_text(self) -> str:
        button_text = self.base.text
        Log.log(f"Я Button виконую дію - отримання тексту кнопки з локатором: {self.locator_type} і значенням: {self.locator_value}. Текст: '{button_text}'", LogType.INFO)
        return button_text

    def is_displayed(self) -> bool:
        Log.log(f"Виконую дію - перевірка видимості кнопки з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base.is_displayed()

    def is_enabled(self) -> bool:
        Log.log(f"Виконую дію - перевірка доступності кнопки з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base.is_enabled()

    def get_base(self) -> WebElement:
        Log.log(f"Виконую дію - повернення базового WebElement кнопки з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.main.core.Log import Log, LogType


class Link:
    def __init__(self, tuple):
        self.base = tuple[0]
        self.locator_type = tuple[1]
        self.locator_value = tuple[2]
        Log.log(f"Я Link знайдений за локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)

    def click(self):
        Log.log(f"Я Link виконую дію - клік на посилання з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        self.base.click()

    def get_text(self) -> str:
        Log.log(f"Я Link виконую дію - отримання тексту посилання з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base.text

    def get_base(self) -> WebElement:
        Log.log(f"Я Link виконую дію - повернення базового WebElement посилання з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base

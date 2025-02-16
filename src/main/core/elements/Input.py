from src.main.core.Log import Log, LogType

class Input:
    def __init__(self, tuple):
        self.base = tuple[0]
        self.locator_type = tuple[1]
        self.locator_value = tuple[2]
        Log.log(f"Я Input знайдений за локатором: {self.locator_type} з значенням: {self.locator_value}", LogType.INFO)

    def write(self, text: str) -> None:
        Log.log(f"Я Input виконую дію - записування тексту '{text}' в поле вводу з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        self.base.send_keys(text)

    def get_search_title(self) -> str:
        Log.log(f"Я Input виконую дію - отримання атрибута 'title' з поля вводу з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base.get_attribute("title")

    def submit(self) -> None:
        Log.log(f"Я Input виконую дію - відправка форми з поля вводу з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        self.base.submit()

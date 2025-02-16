from ..Log import Log, LogType

class Label:
    def __init__(self, tuple):
        self.base = tuple[0]
        self.locator_type = tuple[1]
        self.locator_value = tuple[2]
        Log.log(f"Я Label знайдений за локатором: {self.locator_type} з значенням: {self.locator_value}", LogType.INFO)

    def get_label_text(self) -> str:
        Log.log(f"Я Label виконую дію - отримую текст з локатором: {self.locator_type} і значенням: {self.locator_value}", LogType.INFO)
        return self.base.text

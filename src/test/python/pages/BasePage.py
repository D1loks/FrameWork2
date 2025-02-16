from src.main.core.DriverWrapper import DriverWrapper
from src.main.core.Log import Log, LogType

class BasePage:
    def __init__(self):
        self.driver = DriverWrapper.get_driver()
        self.log_page_title()

    def log_page_title(self):
        """Логує заголовок поточної сторінки"""
        title = self.driver.title
        Log.log(f"Поточна назва сторінки: '{title}'", LogType.INFO)

    def get_title(self) -> str:
        """Повертає заголовок поточної сторінки"""
        return self.driver.title

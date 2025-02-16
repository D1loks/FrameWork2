from src.main.core.Log import Log, LogType
from src.main.core.DriverWrapper import DriverWrapper

class PageNavigationUtil:
    @staticmethod
    def to(page_url: str):
        driver = DriverWrapper()
        Log.log(f"Відкриваємо сторінку {page_url}", LogType.INFO)
        # Додаємо протокол https:// якщо його немає
        if not page_url.startswith(('http://', 'https://')):
            page_url = 'https://' + page_url
        driver.get_driver().get(page_url)
        Log.log(f"Відкрито сторінку {page_url}", LogType.INFO)

    @staticmethod
    def toMainPage():
        driver = DriverWrapper()
        Log.log("Відкриваємо головну сторінку Google", LogType.INFO)
        driver.get_driver().get("https://www.google.com")
        Log.log("Відкрито головну сторінку Google", LogType.INFO)
        return driver

    @staticmethod
    def toSoftserve():
        driver = DriverWrapper()
        Log.log("Відкриваємо сторінку SoftServe", LogType.INFO)
        driver.get_driver().get("https://softserve.ua")
        Log.log("Відкрито сторінку SoftServe", LogType.INFO)
        return driver

    @staticmethod
    def toEpam():
        driver = DriverWrapper()
        Log.log("Відкриваємо сторінку Epam", LogType.INFO)
        driver.get_driver().get("https://www.epam.com")
        Log.log("Відкрито сторінку Epam", LogType.INFO)
        return driver

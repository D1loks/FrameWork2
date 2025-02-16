import logging
import os
from enum import Enum

class LogType(Enum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARNING = "WARNING"

class Log:
    _logger = None

    @classmethod
    def set_name(cls, name: str):
        """Ініціалізація логера з вказаним ім'ям"""
        cls._logger = logging.getLogger(name)
        cls._logger.setLevel(logging.DEBUG)

        # Створюємо форматер
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Додаємо обробник для виводу в консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        cls._logger.addHandler(console_handler)

        # Якщо є файл конфігурації, додаємо обробник для файлу
        log_file = "log4j.properties"
        if os.path.exists(log_file):
            file_handler = logging.FileHandler("app.log")
            file_handler.setFormatter(formatter)
            cls._logger.addHandler(file_handler)

        return cls._logger

    @classmethod
    def get_logger(cls):
        """Повертає логер або створює його, якщо він ще не ініціалізований"""
        if cls._logger is None:
            cls.set_name("default_test")
        return cls._logger

    @classmethod
    def log(cls, message: str, log_type: LogType = LogType.INFO):
        """Логує повідомлення відповідного рівня"""
        logger = cls.get_logger()
        if log_type == LogType.INFO:
            logger.info(message)
        elif log_type == LogType.ERROR:
            logger.error(message)
        elif log_type == LogType.WARNING:
            logger.warning(message)

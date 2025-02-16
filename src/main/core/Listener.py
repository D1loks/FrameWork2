import pytest
import time
from datetime import datetime
from ..utils.screenshot_utils import *
from ..utils.email_utils import send_email
from ..utils.property_utils import get_property
from ..core.Log import Log, LogType

# Глобальна змінна для результатів тестів
suite_result = []

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    """Цей хук виконуватиметься перед початком кожного тесту"""
    Log.log(f"About to begin executing test {item.nodeid}", LogType.INFO)
    item.start_time = time.time()  # Записуємо час початку тесту
    return None  # Продовжуємо виконання тесту

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Цей хук фіксує результати виконання тесту (успіх/невдача)"""
    if call.when == "call":
        duration = time.time() - item.start_time
        if call.excinfo is None:
            # Тест пройшов успішно
            result = f"\nTest {item.nodeid} has passed on {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            suite_result.append(result)
            Log.log(f"Test {item.nodeid} passed in {duration:.2f} seconds", LogType.INFO)
        else:
            # Тест не пройшов
            result = f"\nTest {item.nodeid} has failed on {datetime.now().strftime('%Y-%m-%d %H:%M')}. Error: {call.excinfo[1]}"
            suite_result.append(result)
            Log.log(f"Test {item.nodeid} failed in {duration:.2f} seconds. Error: {call.excinfo[1]}", LogType.ERROR)

            # Знімок екрану при невдачі
            capture_screenshot(item.nodeid)

            # Відправка email (якщо це налаштовано)
            email_enabled = get_property('email')
            if email_enabled.lower() == 'true':
                send_email(f"Test {item.nodeid} failed", result)

    return call  # Повертаємо результат виконання тесту

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Цей хук виконується після завершення сесії тестування"""
    if exitstatus == 0:
        Log.log("All tests passed.", LogType.INFO)
    else:
        Log.log("Some tests failed.", LogType.ERROR)

    # Надсилаємо фінальні результати
    if get_property("email").lower() == "true":
        email_results = "\n".join(suite_result)
        send_email("Test Suite Results", email_results)

@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):
    """Цей хук виконується перед запуском тестів"""
    for item in items:
        Log.log(f"Collecting test {item.nodeid}", LogType.INFO)

    return items

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """Цей хук фіксує звіти про виконання тесту"""
    if report.when == "call":
        Log.log(f"Test {report.nodeid} finished with status {report.outcome}", LogType.INFO)
    return report


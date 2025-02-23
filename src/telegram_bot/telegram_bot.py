import telebot
from telebot import types
import os
import json
import subprocess
from datetime import datetime
import sys
print(sys.executable)
import shutil
# Initialize bot with token
bot = telebot.TeleBot('7817633397:AAGD6gcP5Oan5i2yGWjTd5vMQ1Eep8g4_vM')

# Store chat IDs that should receive notifications
CHAT_IDS = []

# Load chat IDs from file if exists
CHAT_IDS_FILE = 'chat_ids.json'
if os.path.exists(CHAT_IDS_FILE):
    with open(CHAT_IDS_FILE, 'r', encoding='utf-8') as f:
        CHAT_IDS = json.load(f)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in CHAT_IDS:
        CHAT_IDS.append(chat_id)
        with open(CHAT_IDS_FILE, 'w', encoding='utf-8') as f:
            json.dump(CHAT_IDS, f)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('/start'))
    markup.add(types.KeyboardButton('/run'))
    markup.add(types.KeyboardButton('/help'))
    bot.reply_to(message, "Bot started. You will receive test run notifications.", reply_markup=markup)

@bot.message_handler(commands=['run'])
def run_tests(message):
    try:
        # Create timestamp for run name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_name = f"TestRun_{timestamp}"

        # Create log file path
        log_file = f"logs/{run_name}.log"
        os.makedirs("logs", exist_ok=True)

        # Set the test directory path
        test_dir = "C:/Users/danyl/FrameWork/FrameWork2/src/test/python/tests"

        # Execute test run and capture output
        with open(log_file, 'w', encoding='utf-8') as f:
            process = subprocess.run(
                ['C:/Users/danyl/FrameWork/FrameWork2/.venv/Scripts/python.exe', '-m', 'pytest', '--alluredir=allure-results', test_dir, '-v'],
                capture_output=True,
                text=True,
                check=False
            )
            f.write(process.stdout)
            f.write(process.stderr)

        if process.returncode == 0:
            # Count successful tests from output
            test_count = process.stdout.count('PASSED')
            notify_successful_run(run_name, test_count)
            send_allure_report(message, run_name)
        else:
            notify_failed_run(run_name, log_file=log_file)

        bot.reply_to(message, f"Test run '{run_name}' completed")
    except Exception as e:
        bot.reply_to(message, f"Failed to start test run: {str(e)}")

def notify_successful_run(run_name, test_count):
    """Send notification about successful test run"""
    message = (
        f"✅ Successful test run: {run_name}\n"
        f"Total passed tests: {test_count}\n"
        f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    for chat_id in CHAT_IDS:
        bot.send_message(chat_id, message)

def notify_failed_run(run_name, run_url=None, log_file=None):
    """Send notification about failed test run"""
    message = (
        f"❌ Failed test run: {run_name}\n"
        f"Failed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    if run_url:
        message += f"\nRun URL: {run_url}"

    for chat_id in CHAT_IDS:
        bot.send_message(chat_id, message)
        if log_file and os.path.exists(log_file):
            with open(log_file, 'rb') as f:
                bot.send_document(chat_id, f, caption=f"Log file for {run_name}")

def send_allure_report(message, run_name):
    """Архівує та надсилає звіт Allure"""
    report_dir = "allure-results"
    log_file_path = f"logs/{run_name}.log"
    allure_report_dir = "allure-report"
    allure_zip = f"allure-report-{run_name}.zip"

    # Перевіряємо, чи є результати тестування
    if not os.path.exists(report_dir) or not os.listdir(report_dir):
        bot.send_message(message.chat.id, "⚠️ Помилка: Немає даних у allure-results. Можливо, тести не створили звіт.")
        return

    # Генеруємо звіт
    try:
        subprocess.run([
            r'C:\Users\danyl\scoop\shims\allure.CMD', 'generate', report_dir, '-o', allure_report_dir, '--clean'
        ], shell=True, check=True)
        print("✅ Allure report created successfully.")

        # Створюємо ZIP-архів звіту
        shutil.make_archive(f"allure-report-{run_name}", 'zip', allure_report_dir)
        print("✅ Allure report ZIP created successfully.")

        # Надсилаємо ZIP-файл через Telegram
        with open(allure_zip, 'rb') as report_file:
            bot.send_document(message.chat.id, report_file, caption="📊 Allure Report")

        # Надсилаємо лог-файл
        if os.path.exists(log_file_path):
            with open(log_file_path, 'rb') as log_file:
                bot.send_document(message.chat.id, log_file, caption=f"📜 Log file for {run_name}")

        # Видаляємо тимчасовий ZIP-файл
        os.remove(allure_zip)

    except subprocess.CalledProcessError as e:
        bot.send_message(message.chat.id, f"⚠️ Помилка генерації звіту: {str(e)}")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Сталася помилка під час створення звіту: {str(e)}")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """
Available commands:
/start - Start the bot and receive notifications
/run - Start a new test run
/help - Show this help message
    """
    bot.reply_to(message, help_text)

if __name__ == '__main__':
    # Start the bot
    print("Bot started. Press Ctrl+C to stop.")
    bot.infinity_polling()

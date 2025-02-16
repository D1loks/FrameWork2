from selenium import webdriver
import os

def capture_screenshot(test_name):
    driver = webdriver.Chrome()
    screenshot_path = f"screenshots/{test_name}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    driver.quit()

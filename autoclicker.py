import pyautogui
import random

while True:
    # Generate a random interval between clicks (in seconds)
    interval = random.uniform(0.5, 1.5)
    # Perform a left mouse click
    pyautogui.click()
    # Wait for the interval before clicking again
    pyautogui.sleep(interval)


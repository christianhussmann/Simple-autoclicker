import tkinter as tk
import pyautogui
import random
import keyboard


def start_clicking():
    global running
    running = True
    while running:
        # Generate a random interval between clicks (in seconds)
        interval = random.uniform(1, 2)
        # Perform a left mouse click
        pyautogui.click()
        # Wait for the interval before clicking again
        pyautogui.sleep(interval)


def stop_clicking():
    global running
    running = False


root = tk.Tk()
root.title("Autoclicker")

start_button = tk.Button(root, text="Start", command=start_clicking)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_clicking)
stop_button.pack()

keyboard.add_hotkey("F6", start_clicking)
keyboard.add_hotkey("F6", stop_clicking, args=("F6",))

running = False
root.mainloop()

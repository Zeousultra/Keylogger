# Keylogger Project (Ethical & Educational Purpose Only)

## Overview
This Python-based keylogger records all keystrokes and logs them in a uniquely named file based on the timestamp of execution. The project is built **for educational and ethical purposes only** and should be used with **explicit permission** from the system owner.

## Features
- **Logs all keystrokes**, including letters, numbers, and special keys (`[ENTER]`, `[SPACE]`, etc.).
- **Timestamps each keystroke** to maintain accurate order.
- **Creates a unique log file per session** (`keylog_YYYYMMDD_HHMMSS.txt`).
- **Press `ESC` to stop logging**, ensuring an easy exit.
- **Formatted logging** for improved readability.

## Ethical Considerations
🚨 **IMPORTANT:** This keylogger is intended **ONLY** for ethical and educational use. Unauthorized keystroke monitoring is **illegal and unethical**. Always obtain **explicit permission** before using this software.

By using this project, you agree to use it **legally and responsibly**. The creator **is not responsible for any misuse** of this software.

## Requirements
- Python 3.x
- `pynput` library (install using `pip install pynput`)

## Installation & Usage
### Cloning the Repository
If this project is hosted on GitHub, clone it using:
```bash
git clone github.com/Zeousultra/Keylogger
```
Navigate to the project directory:
```bash
cd Keylogger
```

### Running the Keylogger
1. Open a terminal or command prompt.
2. Run the script using:
   ```bash
   python keylogger.py
   ```
3. Press `ESC` to stop logging.
4. The log file will be saved in the same directory.

## Log Files
All keystrokes are saved in a text file named `keylog_<timestamp>.txt` in the project directory. You can open this file to review the recorded keystrokes.

### Example Log Output
```
2025-03-05 14:23:12 - H
2025-03-05 14:23:13 - e
2025-03-05 14:23:14 - l
2025-03-05 14:23:15 - l
2025-03-05 14:23:16 - o
2025-03-05 14:23:17 - [SPACE]
2025-03-05 14:23:18 - W
2025-03-05 14:23:19 - o
2025-03-05 14:23:20 - r
2025-03-05 14:23:21 - l
2025-03-05 14:23:22 - d
2025-03-05 14:23:23 - [ENTER]
```

## Disclaimer
This software **must only be used for ethical and legal purposes**. Unauthorized use is strictly prohibited. **The developer is not responsible for any misuse or legal consequences.**

## License
This project is released under the MIT License.

## Author
Developed by **Athul**.


import pyautogui
import keyboard
import time
import threading

# Global flag to control the auto clicker
clicking = False


def auto_clicker(interval=0.1, button='left'):
    global clicking
    while True:
        if clicking:
            pyautogui.click(button=button)
        time.sleep(interval)


def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Auto-clicking started.")
    else:
        print("Auto-clicking stopped.")


if __name__ == "__main__":
    # Set the key combination to start/stop the auto clicker
    start_stop_key = 'ctrl+shift+c'

    # Start the auto clicker thread
    click_thread = threading.Thread(target=auto_clicker)
    click_thread.daemon = True
    click_thread.start()

    print(f"Press {start_stop_key} to start/stop the auto clicker.")
    keyboard.add_hotkey(start_stop_key, toggle_clicking)

    # Block forever, listening for the hotkey
    keyboard.wait()

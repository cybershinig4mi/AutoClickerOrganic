import time
import threading
import win32api
import win32con

# Define a function that will be used as the autoclicker
def autoclick():
    # Set the delay between clicks in seconds
    delay = 0.5

    # Continuously perform clicks with the specified delay,
    # unless the stop flag is set to True
    while not stop_flag:
        # Use the win32api and win32con modules to perform a left mouse click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        # Sleep for the specified delay
        time.sleep(delay)

# Set the stop flag to False
stop_flag = False

# Start the autoclicker in a separate thread
threading.Thread(target=autoclick).start()

# Prompt the user to press enter to start or stop the autoclicker
input("Press Enter to start/stop the autoclicker: ")

# Toggle the stop flag
stop_flag = not stop_flag

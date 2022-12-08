import time
import threading

# Define a function that will be used as the autoclicker
def autoclick():
    # Set the delay between clicks in seconds
    delay = 0.5

    # Continuously perform clicks with the specified delay
    while True:
        # Perform a mouse click
        mouse.click()

        # Sleep for the specified delay
        time.sleep(delay)

# Start the autoclicker in a separate thread
threading.Thread(target=autoclick).start()

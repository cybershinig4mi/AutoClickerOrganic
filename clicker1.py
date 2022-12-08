import time
import threading


def autoclick():
    
    delay = 0.5

    
    while True:
        # Perform a mouse click
        mouse.click()

        # Sleep for the specified delay
        time.sleep(delay)


threading.Thread(target=autoclick).start()

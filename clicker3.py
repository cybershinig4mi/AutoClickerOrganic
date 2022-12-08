import time
import threading
import ctypes


def autoclick():
    
    delay = 0.5

    
    
    while not stop_flag:
        
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)

        
        time.sleep(delay)


stop_flag = False


threading.Thread(target=autoclick).start()


input("Press Enter to start/stop the autoclicker: ")


stop_flag = not stop_flag
